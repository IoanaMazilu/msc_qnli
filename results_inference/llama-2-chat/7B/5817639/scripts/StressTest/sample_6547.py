distance_premise = float(85)
distance_hypothesis = float(15)

# the hypothesis refers to the distance between two towns, mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance reported in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the distance, and any distance less than or equal to 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
