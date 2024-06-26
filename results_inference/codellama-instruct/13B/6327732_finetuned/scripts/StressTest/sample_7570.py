distance_premise = 45
distance_hypothesis = 35

# the hypothesis refers to the distance between Fred and Sam, mentioned in the premise
if distance_premise <= distance_hypothesis:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
