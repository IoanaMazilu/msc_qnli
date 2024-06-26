distance_premise = 85
distance_hypothesis = 15

# the hypothesis refers to the distance between West-Town and East-Town, mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the distance between West-Town and East-Town
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)