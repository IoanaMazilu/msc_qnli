# Premise: What is the height difference between the two if the Empire State Building is more than 280 m tall and the Petronas Towers is 516 m tall?
# Hypothesis: What is the height difference between the two if the Empire State Building is 480 m tall and the Petronas Towers is 516 m tall?
# Golden Label: neutral

empire_state_building_height_premise = 280
empire_state_building_height_hypothesis = 480
petronas_towers_height_premise = 516
petronas_towers_height_hypothesis = 516

# the hypothesis gives specific heights for the Empire State Building and the Petronas Towers, which are also mentioned in the premise
if empire_state_building_height_hypothesis <= empire_state_building_height_premise:
    # check if the specific height of the Empire State Building in the hypothesis contradicts the estimate of more than 'empire_state_building_height_premise'
    label = "contradiction"
elif petronas_towers_height_hypothesis != petronas_towers_height_premise:
    # check if the height of the Petronas Towers in the hypothesis contradicts the height reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the height of the Empire State Building
    # the specific height given in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

