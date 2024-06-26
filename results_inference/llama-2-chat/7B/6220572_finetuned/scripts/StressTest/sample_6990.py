distance_premise = 12
distance_hypothesis = 52

# the hypothesis refers to the distance the twins ran in opposite directions, also mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the distance in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
