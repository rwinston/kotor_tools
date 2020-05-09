"""
\0	4	DWORD	Resource ID
4	4	DWORD	Flags (BIF index is now in this value, (flags & 0xFFF00000) >> 20). The rest appears to define 'fixed' index.
8	4	DWORD	Offset to Resource Data.
12	4	DWORD	Size of Resource Data.
16	2	WORD	Resource Type
18	2	NULL
"""


class ResourceLocator:
    resref = ''
    rtype = -1
    locator = -1

    def __init__(self, resref, rtype, locator):
        self.resref = resref
        self.rtype = rtype
        self.locator = locator

    def __str__(self):
        return 'ResourceLocator[resref=%s,rtype=%s,locator=%s, nti=%s, sourceIndex=%s]' % (self.resref, self.rtype, self.locator, self.getNonTileSetFileIndex(), self.getSourceIndex())

    """
      bits 31-20: source index (the ordinal value giving the index of the corresponding BIF entry)
            bits 19-14: tileset index
            bits 13- 0: non-tileset file index (any 12 bit value, so long as it matches the value used in the BIF file)
    """
    def getNonTileSetFileIndex(self):
        mask = 0b11111111111111
        return self.locator & mask

    def getSourceIndex(self):
        mask = 0b111111111111
        return (self.locator >> 20) & mask

