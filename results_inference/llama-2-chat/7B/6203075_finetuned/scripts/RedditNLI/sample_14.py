# Defining the variables for the premise and hypothesis
premise_demand_supply = 1.5
hypothesis_demand_supply = 1.5

# The hypothesis and premise mention the demand and supply of oil in the second half of the year
if hypothesis_demand_supply!= premise_demand_supply:
    # Check if the demand and supply values in the hypothesis contradict the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
