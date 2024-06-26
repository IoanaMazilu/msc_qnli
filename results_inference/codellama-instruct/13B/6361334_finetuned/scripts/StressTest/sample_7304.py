premise_mean = 58
hypothesis_mean = 78

# the hypothesis refers to the average golf score of Scott on his first four rounds
# the premise gives the average score as 58, while the hypothesis gives 78
if hypothesis_mean <= premise_mean:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the average golf score
    # any average score greater than 'premise_mean' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
