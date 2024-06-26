scores_premise = [7, 2, 3, 4]
scores_hypothesis = [1, 2, 3, 4]

# the hypothesis refers to the scores mentioned in the premise
if scores_hypothesis!= scores_premise:
    # check if the hypothesis values contradict the scores mentioned in the premise
    label = "contradiction"
else:
    # the hypothesis values are consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
