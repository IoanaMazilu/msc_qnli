premise_score = 80
hypothesis_score = 82

# the hypothesis refers to a higher average than the premise
if hypothesis_score <= premise_score:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific score for the fourth test
    # any score greater than 'premise_score' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
