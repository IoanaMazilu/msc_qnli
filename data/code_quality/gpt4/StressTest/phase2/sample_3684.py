value_premise = 7/12
value_hypothesis = 5/12

# the hypothesis refers to the value Anup was asked to find, which is also mentioned in the premise
if value_premise <= value_hypothesis:
    # check if the 'value_premise' contradicts the estimate of more than 'value_hypothesis'
    label = "contradiction"
elif value_premise != value_hypothesis:
    # check if the 'value_premise' is different to 'value_hypothesis'
    label = "neutral"
else:
    # the premise gives only an estimate for the value
    # any value greater than 'value_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)
