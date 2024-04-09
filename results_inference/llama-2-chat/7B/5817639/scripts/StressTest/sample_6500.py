distance_premise = 45
distance_hypothesis = float(distance_premise) + 10

# the hypothesis refers to the distance traveled by Johnny after Matthew, which is also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance traveled by Johnny in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled by Johnny,
    # any distance greater than the distance mentioned in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
