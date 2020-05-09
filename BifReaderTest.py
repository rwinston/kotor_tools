import os
import unittest

from BifReader import BifReader
from BifResource import BifResource

THIS_DIR = os.path.dirname(__file__)

class BifReaderTest(unittest.TestCase):
    def test_entries(self):
        bif = BifReader(os.path.join(THIS_DIR, 'test/bif/2da.bif'))
        self.assertEqual(bif.entries(), 209)
        res = bif.getResources()[0]
        print(res.data.decode('ascii'))

    def test_signature(self):
        bif = BifReader(os.path.join(THIS_DIR, 'test/bif/2da.bif'))
        self.assertEqual(bif.signature(), 'BIFFV1')


if __name__ == '__main__':
    unittest.main()
