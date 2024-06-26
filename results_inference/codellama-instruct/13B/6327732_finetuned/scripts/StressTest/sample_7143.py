premise_mean = 38
hypothesis_mean = 48

# the hypothesis refers to the average golf score on the first four rounds
if premise_mean <= hypothesis_mean:
    # check if the estimate of 'hypothesis_mean' contradicts the average golf score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average golf score
    # any average golf score greater than 'premise_mean' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)