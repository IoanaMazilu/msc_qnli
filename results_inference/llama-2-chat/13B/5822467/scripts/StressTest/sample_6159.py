empire_state_building_height_premise = 356
petronas_towers_height_premise = 370
empire_state_building_height_hypothesis = 556

# the hypothesis refers to the height difference between the two buildings
if empire_state_building_height_hypothesis - petronas_towers_height_premise > 0:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif empire_state_building_height_hypothesis <= 356:
    # the hypothesis value is less than or equal to the premise value, so no contradiction
    label = "neutral"
else:
    # the premise only gives an estimate for the height difference, so any value greater than 0 is consistent with the premise
    label = "neutral"

print(label)
