from scipy.io import wavfile
from pesq import pesq

rate, ref = wavfile.read(r"C:\Users\alsaf\Desktop\Final-data\Objective-Data\Audio_files\Recording 1\B5_422-122949-0004.wav")
rate, deg = wavfile.read(r"C:\Users\alsaf\Desktop\Final-data\Objective-Data\Audio_files\Recording 1\original_422-122949-0004.wav")

print(pesq(rate, ref, deg, 'wb'))
#print(pesq(rate, ref, deg, 'nb')) wideband == 16Khz


#some stuff u cI could use: 