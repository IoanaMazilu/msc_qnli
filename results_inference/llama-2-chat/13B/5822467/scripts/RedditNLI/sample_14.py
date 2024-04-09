premise_supply = "second half of the year"
premise_demand = "exceed supply"
hypothesis_shortfall = "facing shortfall"

# define variables with representative names for the numerical entities in both inputs
supply_premise = int(premise_supply.split("half")[1])
demand_premise = int(premise_demand.split("exceed")[1])
shortfall_hypothesis = int(hypothesis_shortfall.split("facing")[1])

# extract all quantities as valid numbers (integers or floats)
supply_premise = int(supply_premise)
demand_premise = int(demand_premise)
shortfall_hypothesis = int(shortfall_hypothesis)

# compare the variables
if supply_premise!= shortfall_hypothesis:
    # check if the number of months in the hypothesis contradicts the number of months in the premise
    label = "contradiction"
elif demand_premise > shortfall_hypothesis:
    # check if the estimated demand in the premise exceeds the estimated shortfall in the hypothesis
    label = "entailment"
else:
    # the hypothesis and premise mention the same estimate for the shortfall, so there is no contradiction or entailment
    label = "neutral"

print(label)
