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

# INPUT_200K=$(head -c 204800 $INPUT_PATH > chunk_200K.txt)
# INPUT_400K=$(head -c 409600 $INPUT_PATH > chunk_400K.txt)
# INPUT_600K=$(head -c 614400 $INPUT_PATH > chunk_600K.txt)
# INPUT_800K=$(head -c 819200 $INPUT_PATH > chunk_800K.txt)
# head -c 204800 $INPUT_PATH > chunk_200K.txt
# head -c 409600 $INPUT_PATH > chunk_400K.txt
# head -c 614400 $INPUT_PATH > chunk_600K.txt
# head -c 819200 $INPUT_PATH > chunk_800K.txt
split -b 200K $INPUT_PATH "${OUTPUT_PATH}/chunk_200K_"

# Test file sizes with wc
echo "Size of chunk_200K.txt:"
wc -c < chunk_200K.txt
# echo "Size of chunk_400K.txt:"
# wc -c < chunk_400K.txt
# echo "Size of chunk_600K.txt:"
# wc -c < chunk_600K.txt
# echo "Size of chunk_800K.txt:"
# wc -c < chunk_800K.txt


# Run the dict version using time (with small input)
# (time python "../cs412_foxsays_dict.py" < "../foxsays_t1_in.txt")
# With the bigger inputs:
# (time python "../cs412_foxsays_dict.py" < "chunk_200K.txt")



# Run line_plot.py to create the plots
# Create the plots directory if it doesn't exist
# PLOTS_DIR="plots"
# mkdir -p $PLOTS_DIR

# python "../line_plot.py"
