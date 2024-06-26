distance_premise = 45
distance_hypothesis = 35

# the hypothesis refers to the distance traveled by Johnny, which is also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance traveled by Johnny in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled by Johnny
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
