height_empire_state_building_premise = 356
height_empire_state_building_hypothesis = 556
height_petronas_towers_premise = 370
height_petronas_towers_hypothesis = 370

# the hypothesis refers to the height of the Empire State Building and the Petronas Towers mentioned in the premise
if height_empire_state_building_premise > height_empire_state_building_hypothesis:
    # check if the height of the Empire State Building in the premise contradicts the height in the hypothesis
    label = "contradiction"
elif height_petronas_towers_hypothesis!= height_petronas_towers_premise:
    # check if the height of the Petronas Towers in the hypothesis contradicts the height in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
