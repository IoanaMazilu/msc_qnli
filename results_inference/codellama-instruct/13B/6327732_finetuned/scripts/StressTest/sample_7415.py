premise_land_size = 120
hypothesis_land_size = 220

# the hypothesis refers to the size of the land mentioned in the premise
if hypothesis_land_size <= premise_land_size:
    # check if the estimate of 'hypothesis_land_size' contradicts the size of the land in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of the land
    # any size of land greater than 'premise_land_size' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
