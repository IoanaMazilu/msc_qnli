# Premise: If Henry were to add 6 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Hypothesis: If Henry were to add less than 7 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Golden Label: entailment

water_added_premise = 6
water_added_hypothesis = 7
tank_initial_status_premise = 3/4
tank_initial_status_hypothesis = 3/4
tank_final_status_premise = 7/8
tank_final_status_hypothesis = 7/8

# the hypothesis refers to the same situation described in the premise, but the amount of added water is different
if water_added_hypothesis > water_added_premise:
    # check if the quantity of water in the hypothesis contradicts the quantity of water in the premise
    label = "contradiction"
elif tank_initial_status_hypothesis != tank_initial_status_premise or tank_final_status_hypothesis != tank_final_status_premise:
    # check if the initial or final tank status in the hypothesis contradicts the initial or final tank status in the premise
    label = "contradiction"
else:
    # if the premise does not contradict the hypothesis, we infer neutrality
    # because we don't have enough information to infer entailment
    label = "neutral"
    
print(label)

