distance_premise = 15
distance_hypothesis = 85

# the hypothesis refers to the distance between West-Town and East-Town, mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
else:
    # the premise gives an exact distance, but the hypothesis gives an estimate
    # any distance less than 'distance_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
