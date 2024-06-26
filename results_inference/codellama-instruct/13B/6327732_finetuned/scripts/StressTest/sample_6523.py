subjects_premise = [45, 67, 76, 82, 85]
subjects_hypothesis = [55, 67, 76, 82, 85]

# the hypothesis refers to the same subjects as the premise
if subjects_hypothesis!= subjects_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of subjects
    # any number of subjects greater than'subjects_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
