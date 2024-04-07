# Premise: What is the height difference between the two if the Empire State Building is 443 m tall and the Petronas Towers is 452 m tall?
# Hypothesis: What is the height difference between the two if the Empire State Building is less than 443 m tall and the Petronas Towers is 452 m tall?
# Golden Label: contradiction

empire_state_building_height_premise = 443
empire_state_building_height_hypothesis = 443
petronas_towers_height_premise = 452
petronas_towers_height_hypothesis = 452

# the hypothesis gives the height of the Empire State Building and Petronas Towers, also mentioned in the premise
if empire_state_building_height_hypothesis != empire_state_building_height_premise:
    # check if the height of Empire State Building in the hypothesis contradicts the height given in the premise
    label = "contradiction"
elif petronas_towers_height_hypothesis != petronas_towers_height_premise:
    # check if the height of Petronas Towers in the hypothesis contradicts the height given in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

