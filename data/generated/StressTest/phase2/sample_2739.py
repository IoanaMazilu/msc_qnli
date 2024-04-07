# Premise: Max planned to buy bike, sales man advised him to buy within this month, If he purchase next month means State Tax will be increasing 10% than its cost and it would be 82500.
# Hypothesis: Max planned to buy bike, sales man advised him to buy within this month, If he purchase next month means State Tax will be increasing less than 70% than its cost and it would be 82500.
# Golden Label: entailment

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

