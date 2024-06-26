premise_mean = 38
hypothesis_mean = 48

# the hypothesis refers to the average golf score on Scott's first four rounds
if hypothesis_mean <= premise_mean:
    # check if the estimate of 'hypothesis_mean' contradicts the average score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score less than 'hypothesis_mean' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
