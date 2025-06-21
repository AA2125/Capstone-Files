from pesq import pesq
from scipy.io import wavfile
#import matplotlib.pyplot as plt #might need to plot the recordings
import os
import pandas as pd # so i can store this in a csv file

# Define the directory and original file path
directory = r"C:\Users\alsaf\Desktop\Capstone-Files\Audio_files\Recording 1" # find a way to loop through each folder number x++"
original_file_name = "original_422-122949-0004.wav" # file that is used as a standerd
original_file_path = os.path.join(directory, original_file_name) # path to the original file

# Load the audio file(s) that will be compared.
try:
    deg_sample_rate, deg_audio = wavfile.read(original_file_path)
except Exception as e:
    raise ValueError(f"Error in file: {e}")

# Initialize a dictionary to store results
pesq_scores = {}

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".wav") and filename != original_file_name: # if the audio file name does not match the original file name.
        ref_file_path = os.path.join(directory, filename) # create a new path to audio file
        
        try:
            # Load the reference audio file
            ref_sample_rate, ref_audio = wavfile.read(ref_file_path)
            
            # Ensure both audio files have the same sampling rate (16Khz for both)
            if ref_sample_rate != deg_sample_rate:
                print(f"{filename}: Sampling rates do not match, need to be 16Khz for both bud.")
                continue
            
            #  both audio files should have the same length
            min_length = min(len(ref_audio), len(deg_audio))
            ref_audio_trimmed = ref_audio[:min_length]
            deg_audio_trimmed = deg_audio[:min_length]
            
            # Compute PESQ score (narrowband: 'nb' or wideband: 'wb')
            score = pesq(ref_sample_rate, ref_audio_trimmed, deg_audio_trimmed, 'wb')  # Use 'nb' for narrowband
            pesq_scores[filename] = score
            print(f"PESQ Score for {filename}: {score}")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")


#print the lenghth of audio samples
print(f"Reference Length: {len(ref_audio)}, Anon Systems Length: {len(deg_audio)}")

#final results
print("\nPESQ Scores Summary:")
for file, score in pesq_scores.items():
    print(f"{file}: {score}")