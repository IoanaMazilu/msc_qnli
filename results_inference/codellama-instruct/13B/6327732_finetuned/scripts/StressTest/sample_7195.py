distance_premise = 6
distance_hypothesis = 7

# the hypothesis refers to the exact distance between Chennai and Jammu, mentioned in the premise
if distance_hypothesis!= distance_premise:
    # check if the hypothesis value contradicts the exact distance in the premise
    label = "contradiction"
else:
    # the premise gives an exact distance and the hypothesis gives an exact distance, which can be explicitly entailed from the premise
    label = "entailment"

print(label)
