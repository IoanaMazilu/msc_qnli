premise_score = 80
hypothesis_score = 87

# the hypothesis refers to the number of points Jerry needs to raise his average
if hypothesis_score - premise_score < 7:
    # check if the hypothesis value contradicts the estimate of 'premise_score'
    label = "contradiction"
else:
    # the premise gives only an estimate for the score Jerry needs to earn
    # any score greater than 'premise_score' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
