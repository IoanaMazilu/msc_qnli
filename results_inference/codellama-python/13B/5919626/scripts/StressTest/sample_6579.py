man_weight_premise = 200
man_weight_hypothesis = 100

# the hypothesis refers to the weight of the man mentioned in the premise
if man_weight_premise <= man_weight_hypothesis:
    # check if the estimate of'man_weight_hypothesis' contradicts the weight of the man in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of the man
    # any weight greater than'man_weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
