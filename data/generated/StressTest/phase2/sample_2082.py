# Premise: If Henry were to add 4 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Hypothesis: If Henry were to add more than 3 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Golden Label: entailment

water_added_premise = 4
water_added_hypothesis = 3
tank_status_after_adding_premise = 7 / 8
tank_status_after_adding_hypothesis = 7 / 8

# the hypothesis talks about the amount of water Henry adds to a tank and the tank status after adding, both mentioned in the premise
if water_added_hypothesis >= water_added_premise:
    # check if the hypothesis value contradicts the premise value of 'water_added_premise'
    label = "contradiction"
elif tank_status_after_adding_hypothesis != tank_status_after_adding_premise:
    # check if the hypothesis value contradicts the premise value of 'tank_status_after_adding_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

