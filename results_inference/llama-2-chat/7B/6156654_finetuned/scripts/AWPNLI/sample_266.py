music_files_premise = 4.0
video_files_premise = 21.0
deleted_files = 23.0
files_left = 2.0

# the hypothesis refers to the number of files left on the flash drive, which can be calculated from the premise
# the hypothesis value is less than the deleted files value, which is consistent with the premise
# but the hypothesis does not provide any information about the number of music files or video files

if music_files_premise!= files_left:
    label = "contradiction"
elif video_files_premise!= files_left:
    label = "contradiction"
elif deleted_files!= files_left:
    label = "contradiction"
else:
    label = "entailment"

print(label)
