premise_mean = 38
hypothesis_mean = 38

# the hypothesis refers to the average score on the first four rounds
if hypothesis_mean < premise_mean:
    # check if the hypothesis value contradicts the premise estimate
    label = "contradiction"
else:
    # the premise gives an estimate for the average score
    # any average score greater than or equal to 'premise_mean' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
