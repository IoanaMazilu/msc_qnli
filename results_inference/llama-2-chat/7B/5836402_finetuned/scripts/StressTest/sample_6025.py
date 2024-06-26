percentage_given_back_premise = 6
percentage_given_back_hypothesis = 4

# the hypothesis refers to the percentage given back to parents, which is also mentioned in the premise
if percentage_given_back_hypothesis <= percentage_given_back_premise:
    # check if the hypothesis value contradicts the estimate of more than 'percentage_given_back_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage given back
    # any percentage given back less than 'percentage_given_back_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
