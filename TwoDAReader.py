import struct
from typing import List

from BifResource import BifResource

"""
2DA 
The basic structure of a .2da is a table (rows and columns) of text.
The first two lines in the file are header information that the game finds important, but that humans tend to ignore. 
The third line contains column headings, which are used to reference the data from within scripts (with the command Get2DAString()). 
The remaining lines are the rows of data, numbered starting at 0 (so row 0 is the fourth line in the file). 
The first column of each row is supposed to be the row number, which is information that humans tend to find important, 
but that the game ignores. (The game counts rows as it reads the file, so it has no need for explicit row numbers.) 
There is no column heading for this first column. The remaining columns contain the interesting data.
"""


class TwoDAReader:
    data = []
    sig = ''
    resources = []

    def __init__(self, filename):
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
            print(res)
            self.resources.append(res)

    def signature(self):
        return self.sig

    def entries(self):
        return len(self.resources)

    def resources(self) -> List[BifResource]:
        return self.resources




