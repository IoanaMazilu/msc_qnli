bonds_denomination_premise = "50"
bonds_denomination_hypothesis = "10"

# the hypothesis talks about the denominations of bonds, which is also referenced in the premise
if bonds_denomination_hypothesis <= bonds_denomination_premise:
    # check if the hypothesis value contradicts the estimate of the denominations in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the denominations
    # any denomination greater than 'bonds_denomination_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
