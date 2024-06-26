premise_ratio = 1.5
hypothesis_ratio = 4.0

# the hypothesis refers to the ratio of distances between A to B and B to C
if hypothesis_ratio <= premise_ratio:
    # check if the hypothesis value contradicts the estimate of more than 'premise_ratio'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of distances
    # any ratio greater than 'premise_ratio' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
