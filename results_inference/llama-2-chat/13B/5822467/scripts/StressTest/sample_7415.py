land_area_premise = 120
land_area_hypothesis = 220

# the hypothesis refers to the area of the land, which is also mentioned in the premise
if land_area_premise <= land_area_hypothesis:
    # check if the estimate of 'land_area_hypothesis' contradicts the area of the land reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the area of the land
    # any area greater than 'land_area_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
