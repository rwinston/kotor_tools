import struct
from typing import List

from BifResource import BifResource

"""
BIF file format reader
*0x0000	4 (char array)	Signature ('BIFF')
0x0004	4 (char array)	Version ('V1  ')
0x0008	4 (dword)	Count of file entries
0x000c	4 (dword)	Count of tileset entries
0x0010	4 (dword)	Offset (from start of file) to file entries
"""


class BifReader:

    def __init__(self, filename):
        self.data = []
        self.sig = ''
        self.resources = []
        self.read(filename)

    def read(self, filename):
        with open(filename, "rb") as bif:
            self.data = bif.read()

        offset = 0
        self.sig = str(self.data[:8].decode('ascii').strip())
        offset += 8
        entries = struct.unpack("I", self.data[offset:offset+4])[0]
        offset += 8  # skip 4 NULL bytes
        offset = struct.unpack("I", self.data[offset:offset + 4])[0]

        for i in range(entries):
            locator = struct.unpack('I', self.data[offset:offset+4])[0]
            offset += 4
            roffset = struct.unpack('I', self.data[offset:offset+4])[0]
            offset += 4
            rlen = struct.unpack('I', self.data[offset:offset+4])[0]
            offset += 4
            rtype = struct.unpack('H', self.data[offset:offset+2])[0]
            offset += 4  # skip 2-byte type field and 2-byte null padding
            res = BifResource(locator, self.data[roffset:(roffset+rlen)], rtype)
            self.resources.append(res)

    def signature(self):
        return self.sig

    def entries(self):
        return len(self.resources)

    def getResources(self) -> List[BifResource]:
        return self.resources




