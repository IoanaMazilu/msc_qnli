music_files_premise = 4.0
video_files_premise = 21.0
deleted_files_premise = 23.0
files_left_hypothesis = 0.0

# the hypothesis refers to the number of files left on the flash drive, which can be inferred from the premise
# compute the number of files left on the flash drive in the premise
files_left_premise = music_files_premise + video_files_premise - deleted_files_premise
if files_left_hypothesis!= files_left_premise:
    # check if the number of files left in the hypothesis contradicts the number of files left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
