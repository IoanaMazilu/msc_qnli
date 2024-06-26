distance_premise = 35
distance_hypothesis = 45

# the hypothesis refers to the distance covered by Matthew and Johnny mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance covered in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
