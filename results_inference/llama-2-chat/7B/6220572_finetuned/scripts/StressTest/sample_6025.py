percentage_given_back_premise = 6
percentage_given_back_hypothesis = 4

# the hypothesis refers to the percentage of the amount given back each month, also referenced in the premise
if percentage_given_back_hypothesis <= percentage_given_back_premise:
    # check if the hypothesis value contradicts the estimate of more than 'percentage_given_back_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of the amount given back
    # any percentage greater than 'percentage_given_back_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
