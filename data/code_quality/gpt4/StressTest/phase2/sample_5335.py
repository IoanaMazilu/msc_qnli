value_premise = 5/12
value_hypothesis = 7/12

# the hypothesis refers to the fraction of money Anup was asked to find, which is also mentioned in the premise
if value_hypothesis <= value_premise:
    # check if the fraction in the hypothesis contradicts the estimate of more than 'value_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the fraction of the money
    # any fraction greater than 'value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
