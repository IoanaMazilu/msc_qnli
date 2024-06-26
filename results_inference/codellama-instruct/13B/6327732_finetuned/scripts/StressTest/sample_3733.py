distance_premise = 8
distance_hypothesis = 7

# the hypothesis refers to the distance traveled by Kiran, mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
