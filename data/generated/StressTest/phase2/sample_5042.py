# Premise: What is the height difference between the two if the Empire State Building is 464 m tall and the Petronas Towers is 472 m tall?
# Hypothesis: What is the height difference between the two if the Empire State Building is 764 m tall and the Petronas Towers is 472 m tall?
# Golden Label: contradiction

empire_state_building_height_premise = 464
petronas_towers_height_premise = 472
empire_state_building_height_hypothesis = 764
petronas_towers_height_hypothesis = 472

# the hypothesis refers to the height of the Empire State Building and Petronas Towers mentioned in the premise
if empire_state_building_height_hypothesis != empire_state_building_height_premise or petronas_towers_height_hypothesis != petronas_towers_height_premise:
    # check if the height of Empire State Building or Petronas Towers in the hypothesis contradicts the heights reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

