score_premise = 10
score_hypothesis = 30

# the hypothesis refers to a future test, while the premise refers to the current score
if score_hypothesis <= score_premise:
    # check if the estimate of'score_hypothesis' contradicts the current score reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the current score,
    # any score greater than'score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
