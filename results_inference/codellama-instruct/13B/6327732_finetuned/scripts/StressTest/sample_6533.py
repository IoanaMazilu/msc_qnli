passengers_premise = 37300000
passengers_hypothesis = 37300000

# the hypothesis refers to the number of airline passengers mentioned in the premise
if passengers_premise <= passengers_hypothesis:
    # check if the estimate of 'passengers_hypothesis' contradicts the number of airline passengers in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of airline passengers
    # any number of airline passengers greater than 'passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
