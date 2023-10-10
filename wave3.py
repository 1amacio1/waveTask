import wave
import struct
source = wave.open("in.wav", mode="rb")
dest = wave.open("out.wav", mode="wb")
dest.setparams(source.getparams())


frames_count = source.getnframes()
data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))\

newdata = []
for i in range(len(data)):
    newdata.append(data[i] // 10)

newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)

dest.writeframes(newframes)
source.close()
dest.close()