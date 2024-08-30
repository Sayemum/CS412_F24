#!/bin/bash

source /opt/anaconda3/bin/activate && conda activate /opt/anaconda3/envs/cs412f24

# Use split, wc, and head to create input file sizes
INPUT_PATH="../foxsays_tleader_in.txt"
OUTPUT_PATH="output"
SIZES=(200 400 600 800)

# Create the output directory if it doesn't exist
mkdir -p $OUTPUT_PATH

# Use `split` to create chunks of the specified sizes
for size in "${SIZES[@]}"; do
    split -b ${size}K $INPUT_PATH "${OUTPUT_PATH}/part_${size}K.txt"
done

echo "Files created in $OUTPUT_PATH:"
ls -lh $OUTPUT_PATH