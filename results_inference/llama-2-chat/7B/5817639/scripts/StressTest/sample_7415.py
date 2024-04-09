land_area_premise = 120
land_area_hypothesis = 220

# the hypothesis refers to a larger area of land than the premise
if land_area_premise <= land_area_hypothesis:
    # check if the estimate of 'land_area_hypothesis' contradicts the number of square feet in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the area of land,
    # any larger area of land is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
