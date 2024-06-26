oil_ounces_premise = 7
oil_ounces_hypothesis = 8

# the hypothesis talks about the amount of oil for each cylinder, referenced also in the premise
if oil_ounces_hypothesis <= oil_ounces_premise:
    # check if the hypothesis value contradicts the estimate of more than 'oil_ounces_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of oil ounces
    # any number of oil ounces greater than 'oil_ounces_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
