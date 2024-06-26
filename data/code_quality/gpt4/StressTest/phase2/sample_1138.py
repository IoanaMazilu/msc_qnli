height_empire_state_premise = 743
height_empire_state_hypothesis = 443
height_petronas_premise = 452
height_petronas_hypothesis = 452

# the hypothesis refers to the heights of the Empire State Building and the Petronas Towers mentioned in the premise
if height_empire_state_hypothesis >= height_empire_state_premise:
    # check if the height of the Empire State Building in the hypothesis contradicts the maximum value mentioned in the premise
    label = "contradiction"
elif height_petronas_hypothesis != height_petronas_premise:
    # check if the height of the Petronas Towers in the hypothesis contradicts the height mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, but the exact height of the Empire State Building is not specified in the premise
    label = "neutral"

print(label)
