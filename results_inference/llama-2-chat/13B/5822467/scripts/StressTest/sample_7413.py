land_area_premise = 120
land_area_hypothesis = 320

# the hypothesis refers to the area of the land, which is also mentioned in the premise
if land_area_premise <= land_area_hypothesis:
    # check if the estimate of 'land_area_hypothesis' contradicts the area of the land in the premise
    label = "contradiction"
elif land_area_hypothesis < land_area_premise:
    # check if the hypothesis value contradicts the area of the land reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
