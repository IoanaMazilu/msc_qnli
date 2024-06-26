premise_mean = 48
hypothesis_mean = 38

# the hypothesis refers to the average golf score on the first four rounds
if hypothesis_mean <= premise_mean:
    # check if the hypothesis value contradicts the estimate of less than 'premise_mean'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average golf score
    # any average golf score greater than 'premise_mean' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
