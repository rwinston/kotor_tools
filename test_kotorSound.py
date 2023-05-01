import os
import unittest


from kotorSound import SoundReader

THIS_DIR = os.path.dirname(__file__)


class KotorSoundTest(unittest.TestCase):

    def test_read_2da(self):
        reader = SoundReader()
        reader.readSound('test/vo/vo1.wav')




if __name__ == '__main__':
    unittest.main()