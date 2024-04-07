# Premise: If gas costs $less than 6/gallon, then how many miles can Dan’s car go on $54 of gas?
# Hypothesis: If gas costs $4/gallon, then how many miles can Dan’s car go on $54 of gas?
# Golden Label: neutral

gas_cost_premise = 6
gas_cost_hypothesis = 4
gas_amount = 54

# the hypothesis refers to the cost of gas mentioned in the premise
if gas_cost_hypothesis >= gas_cost_premise:
    # check if the cost of gas in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the cost of gas in the hypothesis is less than the cost in the premise, we can infer entailment
    label = "entailment"

print(label)

