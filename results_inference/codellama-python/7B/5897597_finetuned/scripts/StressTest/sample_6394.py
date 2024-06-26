oil_premise = 7
oil_hypothesis = 8

# the hypothesis refers to the amount of oil George's car needs, which is also mentioned in the premise
if oil_hypothesis <= oil_premise:
    # check if the hypothesis value contradicts the estimate of more than 'oil_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of oil
    # any amount of oil greater than 'oil_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
