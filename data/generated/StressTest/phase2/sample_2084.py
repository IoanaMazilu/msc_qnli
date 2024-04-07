# Premise: If Henry were to add 4 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Hypothesis: If Henry were to add 3 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Golden Label: contradiction

gallons_added_premise = 4
tank_fullness_premise = 7/8
gallons_added_hypothesis = 3
tank_fullness_hypothesis = 7/8

# the hypothesis refers to the amount of water added to the tank and the final fullness of the tank
if gallons_added_hypothesis != gallons_added_premise:
    # check if the amount of water added in the hypothesis contradicts the amount of water added in the premise
    label = "contradiction"
elif tank_fullness_hypothesis != tank_fullness_premise:
    # check if the final fullness of the tank in the hypothesis contradicts the final fullness of the tank in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we cannot infer entailment or contradiction
    label = "neutral"

print(label)

