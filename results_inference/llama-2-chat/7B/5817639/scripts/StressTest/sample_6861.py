distance_premise = 45
distance_hypothesis = 35

# the hypothesis talks about the distance traveled by Johnny after Matthew started walking
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance traveled by Matthew in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled by Matthew
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
