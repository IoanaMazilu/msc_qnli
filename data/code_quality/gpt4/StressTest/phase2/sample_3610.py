avg_marks_four_subjects_premise = 40
avg_marks_four_subjects_hypothesis = 20

# the hypothesis refers to the average marks scored by Ganesh in four subjects, mentioned also in the premise
if avg_marks_four_subjects_hypothesis >= avg_marks_four_subjects_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'avg_marks_four_subjects_premise'
    label = "contradiction"
else:
    # the premise provides an estimate for the difference in average marks 
    # any difference less than 'avg_marks_four_subjects_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
