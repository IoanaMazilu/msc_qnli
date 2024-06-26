premise_mean = 58
hypothesis_mean = 78

# the hypothesis refers to the average golf score on the first four rounds
if hypothesis_mean <= premise_mean:
    # check if the estimate of 'hypothesis_mean' contradicts the average score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score greater than 'premise_mean' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
