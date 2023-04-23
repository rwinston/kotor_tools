import os
import unittest

from TwoDA import TwoDaBReader

THIS_DIR = os.path.dirname(__file__)


class TwoDAReaderTest(unittest.TestCase):

    def test_read_2da(self):
        reader = TwoDaBReader()
        tab = reader.read_from_file(os.path.join(THIS_DIR, 'test/2da/gamma.2da'))
        self.assertEqual(5, len(tab.headers))
        self.assertListEqual([' ', 'desc', 'minimum', 'maximum', 'default'], tab.headers)
        self.assertEqual(3, len(tab.rows))


if __name__ == '__main__':
    unittest.main()