import unittest

from BifReader import BifReader
from BifResource import BifResource
import os

from KeyReader import KeyReader

THIS_DIR = os.path.dirname(__file__)


class KeyReaderTest(unittest.TestCase):
    def test_entries(self):
        key = KeyReader(os.path.join(THIS_DIR, 'test/key/chitin.key'))
        file = open("c:/temp/res", "w")

        file.write('RESOURCES\n')
        for res in key.getResourceLocators():
            file.write('%s > %s (located in %s)\n' % (res, BifResource.resourceMap[res.rtype],key.getBifResourceLocators()[res.getSourceIndex()]))

        file.write('RESOURCES\n')
        for res in key.getBifResourceLocators():
            file.write('%s\n' % res)

        file.close()


if __name__ == '__main__':
    unittest.main()
