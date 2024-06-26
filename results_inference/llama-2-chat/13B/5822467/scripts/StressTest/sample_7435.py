more_than_70_premise = float(input("Premise: Store Z:$more than 70, a 20% sales tax, and $10 rebate after tax"))
90_hypothesis = float(input("Hypothesis: Store Z:$90, a 20% sales tax, and $10 rebate after tax"))

# Extract the numerical values from the premise and hypothesis
sales_tax_premise = more_than_70_premise * 0.2
sales_tax_hypothesis = 90 * 0.2
rebate_premise = more_than_70_premise - sales_tax_premise
rebate_hypothesis = 90 - sales_tax_hypothesis

# Perform calculations
total_cost_premise = sales_tax_premise + rebate_premise
total_cost_hypothesis = sales_tax_hypothesis + rebate_hypothesis

# Compare the total costs
if total_cost_hypothesis <= total_cost_premise:
    # The hypothesis is consistent with the premise, so the label is neutral
    print("neutral")
elif total_cost_hypothesis > total_cost_premise:
    # The hypothesis contradicts the premise
    print("contradiction")
else:
    # The premise and hypothesis have the same total cost, so the label is entailment
    print("entailment")
