# Define variables for the premise and hypothesis
miles_jog_premise = 1
hours_jog_walk_premise = 1
miles_jog_hypothesis = 3
hours_jog_walk_hypothesis = 3

# Check if the hypothesis values contradict the premise
if miles_jog_hypothesis <= miles_jog_premise:
    # The hypothesis value contradicts the premise, so the hypothesis is a contradiction
    label = "contradiction"
elif hours_jog_walk_hypothesis <= hours_jog_walk_premise:
    # The hypothesis value contradicts the premise, so the hypothesis is a contradiction
    label = "contradiction"
else:
    # The hypothesis values do not contradict the premise, so the hypothesis is neutral
    label = "neutral"

print(label)
