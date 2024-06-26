height_empire_state_building_premise = 356
height_petronas_towers_premise = 370
height_empire_state_building_hypothesis = 556
height_petronas_towers_hypothesis = 370

# the hypothesis refers to the height difference between the two buildings mentioned in the premise
if height_empire_state_building_hypothesis - height_petronas_towers_hypothesis <= height_empire_state_building_premise - height_petronas_towers_premise:
    # check if the estimate of 'height_empire_state_building_hypothesis' contradicts the height difference in the premise
    label = "contradiction"
elif height_petronas_towers_hypothesis!= height_petronas_towers_premise:
    # check if the height difference in the hypothesis contradicts the height difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
