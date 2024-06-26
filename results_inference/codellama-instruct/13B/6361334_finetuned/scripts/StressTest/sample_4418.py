premise_score = 2
hypothesis_score = 5

# the hypothesis refers to the number of points Jerry wants to raise his average by
# the premise mentions the score he must earn on the fourth test
if hypothesis_score <= premise_score:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the score Jerry must earn
    # any score greater than 'premise_score' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
