empire_state_building_height_premise = 435
petronas_towers_height_premise = 458
empire_state_building_height_hypothesis = 635
petronas_towers_height_hypothesis = 458

# the hypothesis refers to the heights of the Empire State Building and the Petronas Towers mentioned in the premise
if empire_state_building_height_premise > empire_state_building_height_hypothesis:
    # check if the height estimate of 'empire_state_building_height_premise' contradicts the height of Empire State Building in the hypothesis
    label = "contradiction"
elif petronas_towers_height_hypothesis != petronas_towers_height_premise:
    # check if the height of Petronas Towers in the hypothesis contradicts the height of Petronas Towers reported in the premise
    label = "contradiction"
elif empire_state_building_height_premise == empire_state_building_height_hypothesis:
    # check if the height of Empire State Building in the hypothesis fully and explicitly entails the height of Empire State Building in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
