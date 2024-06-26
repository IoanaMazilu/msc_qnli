sheep_horses_ratio_premise = 1 / 7
sheep_horses_ratio_hypothesis = 6 / 7

# the hypothesis refers to the ratio between sheep and horses at the Stewart farm, which is also mentioned in the premise
if sheep_horses_ratio_hypothesis <= sheep_horses_ratio_premise:
    # check if the hypothesis ratio contradicts the premise ratio
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between sheep and horses
    # any ratio greater than'sheep_horses_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
