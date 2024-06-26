distance_premise = 15
distance_hypothesis = 35

# the hypothesis refers to a different distance between the two people compared to the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between the two people
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
