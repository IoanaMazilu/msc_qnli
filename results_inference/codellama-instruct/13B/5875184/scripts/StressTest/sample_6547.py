distance_premise = 85
distance_hypothesis = 15

# the hypothesis refers to the exact distance between West-Town and East-Town
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the distance
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
