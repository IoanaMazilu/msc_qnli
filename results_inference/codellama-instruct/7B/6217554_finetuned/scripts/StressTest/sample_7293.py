capital_premise = 300
capital_hypothesis = 600

if capital_hypothesis <= capital_premise:
    # check if the hypothesis value contradicts the estimate of more than 'capital_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for James' capital
    # any number of capital greater than 'capital_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
