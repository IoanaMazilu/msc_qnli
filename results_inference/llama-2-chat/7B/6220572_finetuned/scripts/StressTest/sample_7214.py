scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [1, 2, 3, 4, 5]

# the hypothesis refers to the scores mentioned in the premise
if any(score for score in scores_hypothesis if score not in scores_premise):
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of scores
    # any number of scores less than'scores_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
