land_area_premise = 120
land_area_hypothesis = 320

# the hypothesis talks about the area of the land, referenced also in the premise
if land_area_hypothesis <= land_area_premise:
    # check if the hypothesis value contradicts the estimate of more than 'land_area_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the area of the land
    # any area of land greater than 'land_area_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
