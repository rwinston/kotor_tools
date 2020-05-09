"""
\0	4	DWORD	Resource ID
4	4	DWORD	Flags (BIF index is now in this value, (flags & 0xFFF00000) >> 20). The rest appears to define 'fixed' index.
8	4	DWORD	Offset to Resource Data.
12	4	DWORD	Size of Resource Data.
16	2	WORD	Resource Type
18	2	NULL
"""


class BifResourceLocator:

    sz = -1
    filename = ''
    flags = -1
    ordinal = -1

    def __init__(self, sz, filename, flags, ordinal):
        self.sz = sz
        self.filename = filename
        self.flags = flags
        self.ordinal = ordinal

    def __str__(self):
        return 'BifResourceLocator[name=%s,length=%s,flags=%s,ordinal=%s]' % (self.filename, self.sz, self.flags, self.ordinal)

