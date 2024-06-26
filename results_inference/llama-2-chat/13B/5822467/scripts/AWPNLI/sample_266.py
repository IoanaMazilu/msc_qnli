files_premise = 4.0
video_files_premise = 21.0
deleted_files_premise = 23.0
files_hypothesis = 2.0

# compute the number of files left on the flash drive after deletion
files_left_premise = files_premise - deleted_files_premise

if files_hypothesis > files_left_premise:
    # check if the number of files in the hypothesis contradicts the number of files left on the flash drive
    label = "contradiction"
elif files_hypothesis!= files_left_premise:
    # check if the number of files in the hypothesis and the number of files left on the flash drive do not match
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
