demand_supply_premise = "second half"
demand_supply_hypothesis = "second half"
increase_production_premise = 1.5
increase_production_hypothesis = 1.5

# the hypothesis and premise mention the time frame and the increase in oil production
if demand_supply_hypothesis!= demand_supply_premise:
    # check if the time frame in the hypothesis contradicts the time frame in the premise
    label = "contradiction"
elif increase_production_hypothesis!= increase_production_premise:
    # check if the increase in production in the hypothesis contradicts the increase in production in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
