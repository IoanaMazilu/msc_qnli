empire_state_building_height_premise = 356
empire_state_building_height_hypothesis = 556
petronas_towers_height_premise = 370
petronas_towers_height_hypothesis = 370

# the hypothesis refers to the height of the Empire State Building, which is also mentioned in the premise
if empire_state_building_height_hypothesis < empire_state_building_height_premise:
    # check if the height of the Empire State Building in the hypothesis contradicts the height in the premise
    label = "contradiction"
elif petronas_towers_height_hypothesis!= petronas_towers_height_premise:
    # check if the height of the Petronas Towers in the hypothesis contradicts the height in the premise
    label = "contradiction"
else:
    # if the heights in the hypothesis do not contradict the heights in the premise, we can infer entailment
    label = "entailment"

print(label)
