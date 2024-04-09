damaged_buildings_premise = "at least one"
damaged_buildings_hypothesis = "at least one"

# the hypothesis mentions the number of damaged buildings, which is also mentioned in the premise
if damaged_buildings_hypothesis!= damaged_buildings_premise:
    # check if the number of damaged buildings in the hypothesis contradicts the number of damaged buildings in the premise
    label = "contradiction"
else:
    # if the hypothesis value and the premise value are the same, we can infer neutrality
    label = "neutral"

print(label)
