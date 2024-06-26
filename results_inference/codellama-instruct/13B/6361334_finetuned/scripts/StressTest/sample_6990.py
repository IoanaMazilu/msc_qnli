distance_premise = 12
distance_hypothesis = 52

# the hypothesis refers to the distance run by the twins, mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance run by the twins in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the distance run by the twins
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
