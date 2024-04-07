# Premise: If Henry were to add 7 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Hypothesis: If Henry were to add 6 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Golden Label: contradiction

water_added_premise = 7
water_added_hypothesis = 6
tank_status_initial = 3/4
tank_status_final = 7/8

# The hypothesis and the premise both discuss about adding water to a tank and the final status of the tank
if water_added_hypothesis != water_added_premise:
    # check if the amount of water added in the hypothesis contradicts the amount of water added in the premise
    label = "contradiction"
elif tank_status_final != tank_status_initial + (water_added_hypothesis / water_added_premise) * (tank_status_final - tank_status_initial):
    # check if the final status of the tank in the hypothesis contradicts the calculated final status of the tank based on the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

