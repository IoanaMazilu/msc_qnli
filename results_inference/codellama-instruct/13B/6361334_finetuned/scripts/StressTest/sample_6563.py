premise_score = 2
hypothesis_score = 2

# the hypothesis refers to the number of points Jerry must earn on the fourth test to raise his average
if hypothesis_score <= premise_score:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of points Jerry must earn
    # any number of points greater than 'premise_score' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
