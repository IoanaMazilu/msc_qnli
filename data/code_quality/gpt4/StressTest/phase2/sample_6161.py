empire_state_building_premise = 356
empire_state_building_hypothesis = 356
petronas_towers_premise = 370
petronas_towers_hypothesis = 370

# the hypothesis refers to the heights of the Empire State Building and Petronas Towers mentioned in the premise
if empire_state_building_premise < empire_state_building_hypothesis:
    # check if the claim of 'empire_state_building_hypothesis' contradicts the height of Empire State Building in the premise
    label = "contradiction"
elif petronas_towers_hypothesis != petronas_towers_premise:
    # check if the height of Petronas Towers in the hypothesis contradicts the height of Petronas Towers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
