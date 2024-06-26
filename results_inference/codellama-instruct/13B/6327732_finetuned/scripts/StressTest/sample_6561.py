premise_score = 80
hypothesis_score = 86

# the hypothesis refers to the score Jerry must earn on the fourth test
# to raise his average by less than 6 points
if hypothesis_score - premise_score < 6:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the score Jerry must earn
    # any score greater than 'premise_score' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
