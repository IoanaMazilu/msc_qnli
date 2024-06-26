music_files_premise = 4.0
video_files_premise = 21.0
deleted_files_premise = 23.0

# the hypothesis talks about the number of files still on the flash drive, which is also referenced in the premise
# compute the total number of files still on the flash drive from the premise
total_files_premise = music_files_premise + video_files_premise - deleted_files_premise

# check if the number of files from the hypothesis contradicts the number of files from the premise
if total_files_hypothesis!= total_files_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)