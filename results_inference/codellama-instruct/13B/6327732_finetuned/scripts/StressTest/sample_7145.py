premise_mean = 38
hypothesis_mean = 38

# the hypothesis refers to the average golf score of Scott on his first four rounds
if hypothesis_mean >= premise_mean:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an estimate for the average golf score of Scott
    # any value less than 'premise_mean' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
