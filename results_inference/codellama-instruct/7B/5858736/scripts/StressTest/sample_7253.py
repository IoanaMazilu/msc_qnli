# Define variables for the numerical entities in the premise and hypothesis
runs_average_premise = 8
runs_average_hypothesis = 4

# Check if the hypothesis value contradicts the premise
if runs_average_hypothesis <= runs_average_premise:
    # The hypothesis value contradicts the premise, so the hypothesis is a contradiction
    label = "contradiction"
else:
    # The hypothesis value does not contradict the premise, so the hypothesis is neutral
    label = "neutral"

print(label)
