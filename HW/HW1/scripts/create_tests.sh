#!/bin/bash

source /opt/anaconda3/bin/activate && conda activate /opt/anaconda3/envs/cs412f24

# Use split, wc, and head to create input file sizes
INPUT_PATH="../foxsays_tleader_in.txt"
OUTPUT_PATH="output"

# Create the output directory if it doesn't exist
# mkdir -p $OUTPUT_PATH

# Get file size in bytes
# TOTAL_SIZE=$(wc -c < $INPUT_PATH)
# wc -c < $INPUT_PATH

INPUT_200K=$(head -c 204800 $INPUT_PATH > chunk_200K.txt)
INPUT_400K=$(head -c 409600 $INPUT_PATH > chunk_400K.txt)
INPUT_600K=$(head -c 614400 $INPUT_PATH > chunk_600K.txt)
INPUT_800K=$(head -c 819200 $INPUT_PATH > chunk_800K.txt)

# Test file sizes with wc
wc -c < chunk_200K.txt
wc -c < chunk_400K.txt
wc -c < chunk_600K.txt
wc -c < chunk_800K.txt