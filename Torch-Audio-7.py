#Tempelate from:https://colab.research.google.com/github/pytorch/audio/blob/gh-pages/main/_downloads/242b4f86f5d51a9a90d3080d8ce32681/squim_tutorial.ipynb
# Copying the tempelate works
#Ran it in google colab cause GPU (too much to handle)
#works for google drive for loop: https://stackoverflow.com/questions/12952410/iterate-folders-on-my-google-drive?rq=1

import os
import torchaudio
import pandas as pd
from torchaudio.pipelines import SQUIM_OBJECTIVE

# Path to audio files
audio_dir = "C:/Users/alsaf/Desktop/Audio_files"
if not os.path.exists(audio_dir):
    os.makedirs(audio_dir)

audio_files = []
for root, dirs, files in os.walk(audio_dir):
    for file in files:
        if file.endswith(".wav"):
            audio_files.append(os.path.join(root, file))




score_data = [] # to hold data or sum 

if audio_files:
    # Load the model
    model = SQUIM_OBJECTIVE.get_model() ########## model

    for file in audio_files:
        print(f"Processing file: {file}")

        # Load audio without sample rate check
        waveform, _ = torchaudio.load(file)

        # Get score (model returns a list of tensors)
        score = model(waveform)

        # Extract score value
        if isinstance(score, list) and len(score) > 0:
            score_value = score[0].item()
        else:
            score_value = score.item()  # If it's already a tensor

        # Append file path and score to the data list
        folder_path = os.path.dirname(file)
        score_data.append({"Folder": folder_path, "File": file, "Score": score_value})




