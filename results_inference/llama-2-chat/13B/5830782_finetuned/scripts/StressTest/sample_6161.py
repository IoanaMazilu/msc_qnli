empire_state_building_height_premise = 356
empire_state_building_height_hypothesis = 356
petronas_towers_height_premise = 370
petronas_towers_height_hypothesis = 370

# the hypothesis talks about the height of the Empire State Building and the Petronas Towers, referenced also in the premise
if empire_state_building_height_hypothesis >= empire_state_building_height_premise:
    # check if the hypothesis value contradicts the estimate of less than 'empire_state_building_height_premise'
    label = "contradiction"
elif petronas_towers_height_hypothesis!= petronas_towers_height_premise:
    # check if the height of Petronas Towers in the hypothesis contradicts the height of Petronas Towers reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the height of Empire State Building
    # any height of Empire State Building less than 'empire_state_building_height_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
