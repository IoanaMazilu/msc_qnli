less_than_63_premise = 63
less_than_63_hypothesis = 13

# the hypothesis refers to the number of people in a BCCI meeting
if less_than_63_hypothesis <= less_than_63_premise:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_63_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people in a BCCI meeting
    # any number of people less than or equal to 13 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
