empire_state_building_height_premise = 356
empire_state_building_height_hypothesis = 556
petronas_towers_height_premise = 370
petronas_towers_height_hypothesis = 370

# the hypothesis refers to the heights of the Empire State Building and the Petronas Towers mentioned in the premise
if empire_state_building_height_premise >= empire_state_building_height_hypothesis:
    # check if the height of the Empire State Building in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
elif petronas_towers_height_premise!= petronas_towers_height_hypothesis:
    # check if the height of the Petronas Towers in the hypothesis contradicts the height reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
