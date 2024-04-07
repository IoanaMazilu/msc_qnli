# Premise: If Henry were to add 5 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Hypothesis: If Henry were to add 6 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Golden Label: contradiction

water_added_premise = 5
water_added_hypothesis = 6
initial_fill = 3/4
final_fill = 7/8

# the hypothesis refers to the amount of water added to a tank and the resulting fill level, same as the premise
if water_added_hypothesis != water_added_premise:
    # check if the amount of water added in the hypothesis contradicts the amount of water added in the premise
    label = "contradiction"
elif initial_fill != final_fill:
    # check if the initial and final fill levels in the hypothesis contradict the initial and final fill levels in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

