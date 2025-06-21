#!/bin/bash

# Create output directory
#mkdir -p "filtered_audio"

# Process all audio files with SoX
for file in ../original/*.{wav,mp3,flac,aiff,aif,ogg,m4a}; do
    if [ -f "$file" ]; then
        # Get filename without path
        filename=$(basename -- "$file")
        new_file="${filename/original_/LP_}"
        # Apply 3.5kHz lowpass filter using sinc
        sox "$file" "./${new_file}" sinc -1.75k
        
        echo "Processed: $file"
    fi
done

echo "Processing complete."
