import pyaudio


class SoundReader:

    VO_HEADER = bytes([
    0x52, 0x49, 0x46, 0x46, 0x32, 0x00, 0x00, 0x00, 0x57, 0x41, 0x56, 0x45, 0x66, 0x6D, 0x74, 0x20,
    0x12, 0x00, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x22, 0x56, 0x00, 0x00, 0x22, 0x56, 0x00, 0x00,
    0x01, 0x00, 0x08, 0x00, 0x00, 0x00, 0x66, 0x61, 0x63, 0x74, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x64, 0x61, 0x74, 0x61, 0x00, 0x00, 0x00, 0x00])

    def readSound(self, filename):
        ftype = 'Unknown'
        with open(filename, mode='rb') as f:
            b = f.read()
            if b[:58] == SoundReader.VO_HEADER:
                ftype = 'VO'
                p = pyaudio.PyAudio()

                # Open stream (2)
                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=1,
                                rate=wf.getframerate(),
                                output=True)


