empire_state_building_height_premise = 356
petronas_towers_height_premise = 370
empire_state_building_height_hypothesis = 556

# the hypothesis refers to the height difference between the two buildings mentioned in the premise
if empire_state_building_height_hypothesis <= empire_state_building_height_premise:
    # check if the hypothesis value contradicts the estimate of more than 'empire_state_building_height_premise'
    label = "contradiction"
elif petronas_towers_height_premise!= 370:
    # check if the height of the Petronas Towers in the hypothesis contradicts the height reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the height difference
    # any height difference greater than 'empire_state_building_height_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
