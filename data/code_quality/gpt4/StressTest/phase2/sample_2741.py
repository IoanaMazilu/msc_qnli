tax_increase_premise = 10
tax_increase_hypothesis = 10
bike_cost_premise = 82500
bike_cost_hypothesis = 82500

# the hypothesis refers to the tax increase and the cost of the bike mentioned in the premise
if tax_increase_premise < tax_increase_hypothesis:
    # check if the tax increase in the hypothesis contradicts the tax increase in the premise
    label = "contradiction"
elif bike_cost_hypothesis != bike_cost_premise:
    # check if the cost of the bike in the hypothesis contradicts the cost of the bike in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
