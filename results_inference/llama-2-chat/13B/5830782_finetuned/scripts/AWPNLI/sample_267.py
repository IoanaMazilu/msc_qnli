music_files_premise = 4.0
video_files_premise = 21.0
deleted_files_premise = 23.0
files_hypothesis = 0.0

# the hypothesis refers to the number of files, which are also mentioned in the premise
# compute the remaining number of files in the premise after deletion
remaining_files_premise = music_files_premise + video_files_premise - deleted_files_premise
if files_hypothesis!= remaining_files_premise:
    # check if the number of files in the hypothesis contradicts the number of remaining files from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
