store_z_premise = 90
store_z_hypothesis = 70

# the hypothesis refers to the cost of the item in Store Z mentioned in the premise
if store_z_hypothesis <= store_z_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise, so we infer neutral
    label = "neutral"

print(label)
