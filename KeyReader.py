import struct
from typing import List

from BifResourceLocator import BifResourceLocator
from ResourceLocator import ResourceLocator

"""
KEY file header format

x0000	4 (char array)	Signature ('KEY ')
0x0004	4 (char array)	Version ('V1  ')
0x0008	4 (dword)	Count of BIF entries
0x000c	4 (dword)	Count of resource entries
0x0010	4 (dword)	Offset (from start of file) to BIF entries
0x0014	4 (dword)	Offset (from start of file) to resource entries
"""


class KeyReader:
    data = []
    sig = ''
    resources = []
    bifResources = []

    def __init__(self, filename):
        self.read(filename)

    def read(self, filename):
        with open(filename, "rb") as bif:
            self.data = bif.read()

        offset = 0
        self.sig = str(self.data[:8].decode('ascii').strip())
        offset += 8
        # Number of BIF entries
        entries = struct.unpack("I", self.data[offset:offset+4])[0]
        offset += 4
        # Number of resource entries
        resourceEntries = struct.unpack("I", self.data[offset:offset + 4])[0]
        offset += 4
        bifOffset = struct.unpack("I", self.data[offset:offset + 4])[0]
        offset += 4
        resourceOffset = struct.unpack("I", self.data[offset:offset + 4])[0]


        """
        BIF Resource Entries
        Offset	Size (data type)	Description
        0x0000	4 (dword)	Length of BIF file
        0x0004	4 (dword)	Offset from start of file to ASCIIZ BIF filename
        0x0008	2 (word)	Length, including terminating NUL, of ASCIIZ BIF filename
        0x000a	2 (word)	The 16 bits of this field are used individually to mark the location of the relevant file.
        
        (MSB) xxxx xxxx ABCD EFGH (LSB)
        Bits marked A to F determine on which CD the file is stored (A = CD6, F = CD1)
        Bit G determines if the file is in the \cache directory
        Bit H determines if the file is in the \data directory
        """
        # BIF entries
        offset = bifOffset
        for i in range(entries):
            fileLength = struct.unpack('I', self.data[offset:offset+4])[0]
            offset += 4
            filenameOffset = struct.unpack('I', self.data[offset:offset+4])[0]
            offset += 4
            filenameLength = struct.unpack('H', self.data[offset:offset+2])[0]
            offset += 2
            locationFlags = struct.unpack('H', self.data[offset:offset+2])[0]
            offset += 2  # skip 2-byte type field and 2-byte null padding
            print('offset=%s, filenameOffset=%s, filenameLength=%s, fileLength=%s' % (offset, filenameOffset, filenameLength, fileLength))
            res = BifResourceLocator(fileLength, self.data[filenameOffset:filenameOffset+filenameLength].decode('ascii'), locationFlags, i)
            self.bifResources.append(res)

        """
        Resource Entries
            Offset	Size (data type)	Description
            0x0000	8 (resref)	Resource name
            0x0008	2 (word)	Resource type
            0x000a	4 (dword)	Resource locator. The IE resource manager uses 32-bit values as a 'resource index', which codifies the source of the resource as well as which source it refers to. The layout of this value is below.
            
            bits 31-20: source index (the ordinal value giving the index of the corresponding BIF entry)
            bits 19-14: tileset index
            bits 13- 0: non-tileset file index (any 12 bit value, so long as it matches the value used in the BIF file)
        """
        offset = resourceOffset
        print(offset)
        for _ in range(resourceEntries):
            resref = self.data[offset:offset+16].decode('ascii')
            offset += 16
            rtype = struct.unpack('H', self.data[offset:offset+2])[0]
            offset += 2
            locator = struct.unpack('I', self.data[offset:offset + 4])[0]
            offset += 4
            resourceLocator = ResourceLocator(resref, rtype, locator)
            self.resources.append(resourceLocator)

    def signature(self):
        return self.sig

    def entries(self):
        return len(self.resources)

    def getBifResourceLocators(self) -> List[BifResourceLocator]:
        return self.bifResources

    def getResourceLocators(self) -> List[ResourceLocator]:
        return self.resources




