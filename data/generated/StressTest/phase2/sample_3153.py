# Premise: If Henry were to add 7 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Hypothesis: If Henry were to add more than 5 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Golden Label: entailment

water_added_premise = 7
water_added_hypothesis = 5
tank_level_premise = 7/8
tank_level_hypothesis = 7/8

# the hypothesis refers to the amount of water added and the tank level mentioned in the premise
if water_added_premise <= water_added_hypothesis:
    # check if the estimate of 'water_added_hypothesis' contradicts the amount of water added in the premise
    label = "contradiction"
elif tank_level_hypothesis != tank_level_premise:
    # check if the tank level in the hypothesis contradicts the tank level reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

