subject_grades_premise = [55, 67, 76, 82, 85]
subject_grades_hypothesis = [35, 67, 76, 82, 85]

# the hypothesis talks about the same set of subjects as the premise
if sum(subject_grades_hypothesis) <= sum(subject_grades_premise):
    # check if the hypothesis value contradicts the estimate of the average of the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the average, and any value greater than that estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
