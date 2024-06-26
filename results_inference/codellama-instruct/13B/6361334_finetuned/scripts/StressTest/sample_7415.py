land_side_premise = 120
land_side_hypothesis = 220

# the hypothesis refers to the size of the land, which is also mentioned in the premise
if land_side_hypothesis <= land_side_premise:
    # check if the estimate of 'land_side_hypothesis' contradicts the size of the land in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
