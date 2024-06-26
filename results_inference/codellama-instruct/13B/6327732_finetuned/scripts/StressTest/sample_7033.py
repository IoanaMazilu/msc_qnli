distance_premise = 800
distance_hypothesis = 100

# the hypothesis refers to the distance between Fred and Sam, mentioned in the premise
if distance_premise <= distance_hypothesis:
    # check if the estimate of 'distance_hypothesis' contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between Fred and Sam
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
