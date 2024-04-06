# Premise: Amy had 4.0 music files and 21.0 video files on her flash drive, and she deleted 23.0 of the files.
# Hypothesis: 2.0 files were still on her flash drive.
# Golden Label: entailment

music_files_premise = 4.0
video_files_premise = 21.0
deleted_files_premise = 23.0
files_left_hypothesis = 2.0

# the hypothesis refers to the number of files, which are also mentioned in the premise
# compute the total number of files in the premise
total_files_premise = music_files_premise + video_files_premise

# compute the number of files left on the flash drive according to the premise
files_left_premise = total_files_premise - deleted_files_premise

if files_left_hypothesis != files_left_premise:
    # check if the number of files left in the hypothesis contradicts the number of files left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

