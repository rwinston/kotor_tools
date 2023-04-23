import io
import struct
from typing import List


class TwoDaTable:
    def __init__(self, headers: List[str]):
        self.headers = headers
        self.rows = []

    def get_column_count(self) -> int:
        return len(self.headers)

    def append_row(self, row: List[str]):
        self.rows.append(row)

    def get_row_count(self) -> int:
        return len(self.rows)

    def get_cell(self, row: int, col: int) -> str:
        return self.rows[row][col]

    def __str__(self):
        rep = ''
        for header in self.headers:
            rep += header+'\t'
        rep += '\n'
        for row in self.rows:
            for obj in row:
                rep += obj + '\t'
            rep += '\n'
        return rep


class TwoDaBReader:
    def __init__(self):
        pass

    @staticmethod
    def read_string_terminated(stream: io.BytesIO, term: int) -> str:
        sb = []
        b = stream.read(1)
        while b != b"" and b != bytes([term]):
            sb.append(chr(ord(b)))
            b = stream.read(1)
        return "".join(sb) if b != b"" else None

    @staticmethod
    def read_string0(buffer: bytes, offset: int) -> str:
        sb = []
        b = buffer[offset]
        while b != 0:
            sb.append(chr(b))
            offset += 1
            b = buffer[offset]
        return "".join(sb)

    @staticmethod
    def read_int_le(stream: io.BytesIO) -> int:
        b = stream.read(4)
        return struct.unpack("<i", b)[0]

    @staticmethod
    def read_from_file(filename: str) -> TwoDaTable:
        with open(filename, "rb") as file:
            stream = io.BytesIO(file.read())
            return TwoDaBReader.read_two_da_binary(stream, True)

    @staticmethod
    def read_two_da_binary(stream: io.BytesIO, with_header: bool) -> TwoDaTable:
        stream = io.BufferedReader(stream)
        if with_header:
            header = TwoDaBReader.read_string_terminated(stream, 0x0a)
            if header is None or header != "2DA V2.b":
                raise IOError("Not a 2DA file!")
        headers = []
        while True:
            s = TwoDaBReader.read_string_terminated(stream, 0x09)
            if s is None:
                break
            headers.append(s)
            b = stream.peek()[0]
            if b == 0:
                stream.read(1)
                break

        headers.insert(0, " ")
        two_da = TwoDaTable(headers)

        rows = TwoDaBReader.read_int_le(stream)

        row_headers = []
        for i in range(rows):
            row_headers.append(TwoDaBReader.read_string_terminated(stream, 0x09))

        index_size = rows * (len(headers)-1) * 2
        index = stream.read(index_size)
        bb = struct.unpack("<%dH" % (len(index) // 2), index)

        data_size = struct.unpack("<H", stream.read(2))[0] # should be 26
        data = stream.read(data_size)

        for i in range(rows):
            row = [None] * two_da.get_column_count()
            row[0] = row_headers[i]
            for j in range(len(headers) - 1):
                bbi = (i * (len(headers)-1)) + j
                s = TwoDaBReader.read_string0(data, bb[bbi]).strip()
                if s == "":
                    s = "****"
                row[j + 1] = s
            two_da.append_row(row)
        return two_da
