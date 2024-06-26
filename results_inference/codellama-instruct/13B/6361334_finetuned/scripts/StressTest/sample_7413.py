land_side_premise = 120
land_side_hypothesis = 320

# the hypothesis refers to the size of the land, mentioned in the premise
if land_side_hypothesis >= land_side_premise:
    # check if the estimate of 'land_side_hypothesis' contradicts the size of the land in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the size of the land
    # any size of land less than 'land_side_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
