empire_state_building_height_premise = 435
petronas_towers_height_premise = 445

# the hypothesis refers to the height difference between the two buildings
hypothesis_height_difference = less_than_435 - empire_state_building_height_premise

# check if the hypothesis value contradicts the premise value
if hypothesis_height_difference <= 0:
    label = "contradiction"
elif petronas_towers_height_premise - empire_state_building_height_premise!= hypothesis_height_difference:
    # check if the number of roses in the hypothesis contradicts the number of roses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
