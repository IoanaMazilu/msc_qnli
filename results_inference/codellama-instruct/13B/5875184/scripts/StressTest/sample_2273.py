premise_ratio = 2/3
hypothesis_ratio = 8/3

# the hypothesis refers to the ratio of distances between A to B and B to C
if hypothesis_ratio > premise_ratio:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of distances
    # any ratio greater than or equal to 'premise_ratio' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
