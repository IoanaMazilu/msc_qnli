scores_premise = [1, 2, 3]
scores_hypothesis = [1, 2, 3]

# the hypothesis refers to the scores mentioned in the premise
if scores_hypothesis <= scores_premise:
    # check if the estimate of'scores_hypothesis' contradicts the scores reported in the premise
    label = "contradiction"
elif scores_hypothesis[0] < scores_premise[0]:
    # check if the first score in the hypothesis contradicts the first score reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores
    # any number of scores less than'scores_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
