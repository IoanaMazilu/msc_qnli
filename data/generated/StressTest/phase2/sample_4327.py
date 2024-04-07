# Premise: Anup was asked to find the value of more than 6/12 of a sum of money R.
# Hypothesis: Anup was asked to find the value of 7/12 of a sum of money R.
# Golden Label: neutral

value_premise = 6/12
value_hypothesis = 7/12

# the hypothesis talks about the value of a certain fraction of money, referenced also in the premise
if value_hypothesis <= value_premise:
    # check if the hypothesis value contradicts the estimate of more than 'value_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the fraction of money
    # any fraction greater than 'value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

