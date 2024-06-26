premise_mean = 18
hypothesis_mean = 38

# the hypothesis refers to the average golf score of Scott on his first four rounds
# the premise gives an estimate for the average score, but does not provide a specific value
if hypothesis_mean <= premise_mean:
    # check if the hypothesis value contradicts the estimate of the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any value greater than 'premise_mean' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
