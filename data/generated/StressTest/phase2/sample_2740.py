# Premise: Max planned to buy bike, sales man advised him to buy within this month, If he purchase next month means State Tax will be increasing less than 70% than its cost and it would be 82500.
# Hypothesis: Max planned to buy bike, sales man advised him to buy within this month, If he purchase next month means State Tax will be increasing 10% than its cost and it would be 82500.
# Golden Label: neutral

tax_increase_premise = 70
tax_increase_hypothesis = 10
bike_cost_premise = 82500
bike_cost_hypothesis = 82500

# the hypothesis refers to the tax increase and bike cost mentioned in the premise
if tax_increase_hypothesis > tax_increase_premise:
    # check if the tax increase in the hypothesis contradicts the tax increase in the premise
    label = "contradiction"
elif bike_cost_hypothesis != bike_cost_premise:
    # check if the bike cost in the hypothesis contradicts the bike cost in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

