"""
\0	4	DWORD	Resource ID
4	4	DWORD	Flags (BIF index is now in this value, (flags & 0xFFF00000) >> 20). The rest appears to define 'fixed' index.
8	4	DWORD	Offset to Resource Data.
12	4	DWORD	Size of Resource Data.
16	2	WORD	Resource Type
18	2	NULL
"""
from collections import defaultdict


class BifResource:
    resourceMap = defaultdict(
        str,
        {
            0x0000: 'res',
            0x0001: 'bmp',
            0x0002: 'mve',
            0x0003: 'tga',
            0x0004: 'wav',
            0x0006: 'plt',
            0x0007: 'ini',
            0x0008: 'mp3',
            0x0009: 'mpg',
            0x000A: 'txt',
            0x000B: 'xml',
            0x07D0: 'plh',
            0x07D1: 'tex',
            0x07D2: 'mdl',
            0x07D3: 'thg',
            0x07D5: 'fnt',
            0x07D7: 'lua',
            0x07D8: 'slt',
            0x07D9: 'nss',
            0x07DA: 'ncs',
            0x07DB: 'mod',
            0x07DC: 'are',
            0x07DD: 'set',
            0x07DE: 'ifo',
            0x07DF: 'bic',
            0x07E0: 'wok',
            0x07E1: '2da',
            0x07E2: 'tlk',
            0x07E6: 'txi',
            0x07E7: 'git',
            0x07E8: 'bti',
            0x07E9: 'uti',
            0x07EA: 'btc',
            0x07EB: 'utc',
            0x07ED: 'dlg',
            0x07EE: 'itp',
            0x07EF: 'btt',
            0x07F0: 'utt',
            0x07F1: 'dds',
            0x07F2: 'bts',
            0x07F3: 'uts',
            0x07F4: 'ltr',
            0x07F5: 'gff',
            0x07F6: 'fac',
            0x07F7: 'bte',
            0x07F8: 'ute',
            0x07F9: 'btd',
            0x07FA: 'utd',
            0x07FB: 'btp',
            0x07FC: 'utp',
            0x07FD: 'dft',
            0x07FE: 'gic',
            0x07FF: 'gui',
            0x0800: 'css',
            0x0801: 'ccs',
            0x0802: 'btm',
            0x0803: 'utm',
            0x0804: 'dwk',
            0x0805: 'pwk',
            0x0806: 'btg',
            0x0808: 'jrl',
            0x0809: 'sav',
            0x080A: 'utw',
            0x080B: '4pc',
            0x080C: 'ssf',
            0x080F: 'bik',
            0x0810: 'ndb',
            0x0811: 'ptm',
            0x0812: 'ptt',
            0x0813: 'ncm',
            0x0814: 'mfx',
            0x0815: 'mat',
            0x0816: 'mdb',
            0x0817: 'say',
            0x0818: 'ttf',
            0x0819: 'ttc',
            0x081A: 'cut',
            0x081B: 'ka',
            0x081C: 'jpg',
            0x081D: 'ico',
            0x081E: 'ogg',
            0x081F: 'spt',
            0x0820: 'spw',
            0x0821: 'wfx',
            0x0822: 'ugm',
            0x0823: 'qdb',
            0x0824: 'qst',
            0x0825: 'npc',
            0x0826: 'spn',
            0x0827: 'utx',
            0x0828: 'mmd',
            0x0829: 'smm',
            0x082A: 'uta',
            0x082B: 'mde',
            0x082C: 'mdv',
            0x082D: 'mda',
            0x082E: 'mba',
            0x082F: 'oct',
            0x0830: 'bfx',
            0x0831: 'pdb',
            0x0832: 'TheWitcherSave',
            0x0833: 'pvs',
            0x0834: 'cfx',
            0x0835: 'luc',
            0x0837: 'prb',
            0x0838: 'cam',
            0x0839: 'vds',
            0x083A: 'bin',
            0x083B: 'wob',
            0x083C: 'api',
            0x083D: 'properties',
            0x083E: 'png',
            0x270B: 'big',
            0x270D: 'erf',
            0x270E: 'bif',
            0x270F: 'key'
        })

    data = []
    rtype = -1
    rid = -1

    def __init__(self, rid, data, rtype):
        self.rid = rid
        self.data = data
        self.rtype = rtype

    def type(self):
        return self.resourceMap[self.type]

    def data(self):
        return self.data

    def __str__(self):
        return 'BifResource[id=%s, len=%s, type=%s]' % (self.rid, len(self.data), self.resourceMap[self.rtype])
