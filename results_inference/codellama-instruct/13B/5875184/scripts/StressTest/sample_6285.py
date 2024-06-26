premise_score = 83
hypothesis_score = 70

# the hypothesis refers to the score on a less than 70th test
if premise_score <= hypothesis_score:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the score
    # any score greater than 'hypothesis_score' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
