value_premise = 4/12
value_hypothesis = 7/12

# the hypothesis talks about the value Anup was asked to find, referenced also in the premise
if value_hypothesis <= value_premise:
    # check if the hypothesis value contradicts the estimate of more than 'value_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the value
    # any value greater than 'value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
