# Premise: If Henry were to add 9 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Hypothesis: If Henry were to add more than 8 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Golden Label: entailment

water_added_premise = 9
water_added_hypothesis = 8
tank_fullness_premise = 7/8
tank_fullness_hypothesis = 7/8

# the hypothesis refers to the amount of water added to a tank mentioned in the premise
if water_added_premise <= water_added_hypothesis:
    # check if the estimate of 'water_added_hypothesis' contradicts the amount of water added in the premise
    label = "contradiction"
elif tank_fullness_hypothesis != tank_fullness_premise:
    # check if the fullness of the tank in the hypothesis contradicts the fullness of the tank reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

