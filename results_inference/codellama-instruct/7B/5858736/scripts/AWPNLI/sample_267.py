# Define variables with representative names for the numerical entities in both inputs
music_files_premise = 4.0
video_files_premise = 21.0
deleted_files_premise = 23.0
files_hypothesis = 0.0

# Extract all quantities as valid numbers (integers or floats)
total_files_premise = music_files_premise + video_files_premise

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments
if deleted_files_premise > total_files_premise:
    # Check if the number of deleted files contradicts the total number of files on the flash drive
    label = "contradiction"
elif files_hypothesis!= 0.0:
    # Check if the number of files on the flash drive contradicts the hypothesis
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
