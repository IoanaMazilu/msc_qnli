# Define variables with representative names for the numerical entities in both inputs
files_premise = 4.0
video_files_premise = 21.0
deleted_files_premise = 23.0
files_hypothesis = 0.0

# Extract all quantities as valid numbers (integers or floats)
files_premise = float(files_premise)
video_files_premise = float(video_files_premise)
deleted_files_premise = float(deleted_files_premise)
files_hypothesis = float(files_hypothesis)

# Comments explaining the comparison
# The hypothesis states that 0 files are still on the flash drive
# The premise states that Amy deleted 23 files, so there should be fewer files left

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments

# Perform calculations if necessary
files_left = files_premise - deleted_files_premise

# Compare the variables
if files_left > files_hypothesis:
    # Check if the number of files left in the premise contradicts the hypothesis
    label = "contradiction"
elif files_left == files_hypothesis:
    # Check if the number of files left in the premise and hypothesis are equal
    label = "entailment"
else:
    # Check if the number of files left in the premise is less than the hypothesis
    label = "contradiction"

# Print the label
print(label)
