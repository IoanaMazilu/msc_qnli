empire_state_building_height_premise = 356
empire_state_building_height_hypothesis = 556
petronas_towers_height_premise = 370
petronas_towers_height_hypothesis = 370

# the hypothesis talks about the heights of the Empire State Building and the Petronas Towers, referenced also in the premise
if empire_state_building_height_hypothesis < empire_state_building_height_premise:
    # check if the hypothesis value contradicts the height of the Empire State Building in the premise
    label = "contradiction"
elif petronas_towers_height_hypothesis != petronas_towers_height_premise:
    # check if the height of the Petronas Towers in the hypothesis contradicts the height of the Petronas Towers in the premise
    label = "contradiction"
elif empire_state_building_height_premise > empire_state_building_height_hypothesis:
    # check if the height of the Empire State Building in the premise contradicts the limit set in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
