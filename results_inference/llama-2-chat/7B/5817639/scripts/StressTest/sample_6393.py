oil_premise = 8
oil_hypothesis = 7

# the hypothesis refers to a different quantity than the premise
if oil_hypothesis <= oil_premise:
    # check if the hypothesis value contradicts the estimate of 'oil_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of oil,
    # any quantity greater than 'oil_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
