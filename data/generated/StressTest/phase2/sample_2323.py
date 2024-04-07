# Premise: If Henry were to add less than 7 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Hypothesis: If Henry were to add 6 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Golden Label: neutral

water_added_premise = 7
water_added_hypothesis = 6
tank_initial_state_premise = 3/4
tank_final_state_premise = 7/8
tank_initial_state_hypothesis = 3/4
tank_final_state_hypothesis = 7/8

# the hypothesis refers to the quantity of water added to the tank and the final state of the tank mentioned in the premise
if water_added_hypothesis >= water_added_premise:
    # check if the amount of water added in the hypothesis contradicts the premise estimate of less than 'water_added_premise'
    label = "contradiction"
elif tank_initial_state_hypothesis != tank_initial_state_premise or tank_final_state_hypothesis != tank_final_state_premise:
    # check if the initial or final tank states in the hypothesis contradict the initial or final tank states reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

