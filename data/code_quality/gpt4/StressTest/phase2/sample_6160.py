empire_state_building_premise = 556
empire_state_building_hypothesis = 356
petronas_towers_premise = 370
petronas_towers_hypothesis = 370

# the hypothesis talks about the height of Empire State Building and Petronas Towers, which are also referenced in the premise
if empire_state_building_hypothesis >= empire_state_building_premise:
    # check if the hypothesis height of Empire State Building contradicts the estimate of less than 'empire_state_building_premise'
    label = "contradiction"
elif petronas_towers_hypothesis != petronas_towers_premise:
    # check if the height of Petronas Towers in the hypothesis contradicts the height of Petronas Towers in the premise
    label = "contradiction"
elif empire_state_building_hypothesis < empire_state_building_premise and petronas_towers_hypothesis == petronas_towers_premise:
    # if the height values in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
