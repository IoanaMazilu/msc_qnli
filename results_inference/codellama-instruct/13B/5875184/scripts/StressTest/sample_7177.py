premise_ratio = 2/4/6
hypothesis_ratio = 2/4/6

# the hypothesis refers to the ration of John, Jose & Binoy
if hypothesis_ratio <= premise_ratio:
    # check if the estimate of 'hypothesis_ratio' contradicts the ration in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ration
    # any ration greater than 'premise_ratio' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
