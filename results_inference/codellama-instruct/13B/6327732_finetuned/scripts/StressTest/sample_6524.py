subjects_premise = [55, 67, 76, 82, 85]
subjects_hypothesis = [35, 67, 76, 82, 85]

# the hypothesis refers to the same subjects as the premise
if subjects_hypothesis!= subjects_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise and hypothesis values are consistent, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
