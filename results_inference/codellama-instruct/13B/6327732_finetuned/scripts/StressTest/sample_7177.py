ration_premise = 2
ration_hypothesis = 4

# the hypothesis refers to the number of people in the ration mentioned in the premise
if ration_premise <= ration_hypothesis:
    # check if the estimate of 'ration_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people in the ration
    # any number of people greater than 'ration_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
