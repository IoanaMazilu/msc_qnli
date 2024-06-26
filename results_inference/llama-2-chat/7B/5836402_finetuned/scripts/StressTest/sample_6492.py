percentage_given_back_premise = 3
percentage_given_back_hypothesis = 7

# the hypothesis refers to the percentage of amount given back to parents, mentioned in the premise
if percentage_given_back_hypothesis <= percentage_given_back_premise:
    # check if the hypothesis value contradicts the estimate of more than 'percentage_given_back_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of amount given back
    # any percentage less than 'percentage_given_back_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
