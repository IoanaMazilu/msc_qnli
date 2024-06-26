tax_premise = 100
tax_hypothesis = 300

# The hypothesis refers to the tax amount added to Harini's pet cost, which is also mentioned in the premise
if tax_hypothesis <= tax_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'tax_premise' from the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the tax amount
    # Any tax amount greater than 'tax_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
