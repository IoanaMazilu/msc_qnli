# Define variables for the premise and hypothesis
miles_jog_premise = 3
hours_jog_walk_premise = 3
miles_jog_hypothesis = 4
hours_jog_walk_hypothesis = 4

# Check if the hypothesis value contradicts the premise
if miles_jog_hypothesis <= miles_jog_premise:
    # The hypothesis value contradicts the premise, so the hypothesis is a contradiction
    label = "contradiction"
elif hours_jog_walk_hypothesis <= hours_jog_walk_premise:
    # The hypothesis value contradicts the premise, so the hypothesis is a contradiction
    label = "contradiction"
else:
    # The hypothesis value does not contradict the premise, so the hypothesis is neutral
    label = "neutral"

print(label)
