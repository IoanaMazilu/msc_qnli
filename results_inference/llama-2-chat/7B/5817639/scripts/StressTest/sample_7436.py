# Define variables for the premise and hypothesis
premise_cost = 90
premise_tax = 0.20
premise_rebate = 10
hypothesis_cost = 0
hypothesis_tax = 0
hypothesis_rebate = 0

# Extract quantities from the premise and hypothesis
quantities = {
    "cost": premise_cost,
    "tax": premise_tax,
    "rebate": premise_rebate,
    "cost_hypothesis": hypothesis_cost,
    "tax_hypothesis": hypothesis_tax,
    "rebate_hypothesis": hypothesis_rebate
}

# Check if the hypothesis cost is less than the premise cost
if quantities["cost_hypothesis"] < quantities["cost"]:
    # The hypothesis contradicts the premise
    label = "contradiction"
elif quantities["tax_hypothesis"] > quantities["tax"]:
    # The hypothesis tax is greater than the premise tax
    label = "contradiction"
elif quantities["rebate_hypothesis"] > quantities["rebate"]:
    # The hypothesis rebate is greater than the premise rebate
    label = "contradiction"
else:
    # The hypothesis values and estimates do not contradict the premise values and estimates
    label = "entailment"

print(label)
