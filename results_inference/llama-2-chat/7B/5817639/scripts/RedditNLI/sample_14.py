# Define variables for the premise and hypothesis
premise_demand = 0
premise_supply = 0
hypothesis_demand = 0
hypothesis_production = 0

# Extract quantities from the premise and hypothesis
premise_demand = float(input("Enter the demand in the premise: "))
premise_supply = float(input("Enter the supply in the premise: "))
hypothesis_demand = float(input("Enter the demand in the hypothesis: "))
hypothesis_production = float(input("Enter the production in the hypothesis: "))

# Compare the quantities
if hypothesis_demand > premise_supply:
    # Check if the hypothesis contradicts the premise
    label = "contradiction"
elif hypothesis_production < 1.5 * premise_supply:
    # Check if the hypothesis entails the premise
    label = "entailment"
else:
    # The hypothesis does not entail or contradict the premise, so the label is "neutral"
    label = "neutral"

print(label)
