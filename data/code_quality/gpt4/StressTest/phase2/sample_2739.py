bike_cost_with_tax_premise = 82500
tax_increase_premise = 10
tax_increase_hypothesis = 70

# the hypothesis and premise refer to the cost of the bike with tax and the percentage increase in tax
if tax_increase_premise >= tax_increase_hypothesis:
    # check if the hypothesis value contradicts the given 'tax_increase_premise'
    label = "contradiction"
else:
    # the premise only gives an estimate of the tax increase
    # any tax increase less than 'tax_increase_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
