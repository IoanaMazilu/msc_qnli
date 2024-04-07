# Premise: What is the height difference between the two if the Empire State Building is 435 m tall and the Petronas Towers is 458 m tall?
# Hypothesis: What is the height difference between the two if the Empire State Building is more than 435 m tall and the Petronas Towers is 458 m tall?
# Golden Label: contradiction

empire_state_building_height_premise = 435
empire_state_building_height_hypothesis = 435
petronas_towers_height_premise = 458
petronas_towers_height_hypothesis = 458

# the hypothesis refers to the height of the buildings mentioned in the premise
if empire_state_building_height_premise != empire_state_building_height_hypothesis:
    # check if the height of Empire State Building in the hypothesis contradicts the height mentioned in the premise
    label = "contradiction"
elif petronas_towers_height_premise != petronas_towers_height_hypothesis:
    # check if the height of Petronas Towers in the hypothesis contradicts the height mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

