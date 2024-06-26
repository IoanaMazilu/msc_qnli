# Define variables for the numerical entities in the premise and hypothesis
runs_average_premise = 8
runs_average_hypothesis = 5

# Check if the hypothesis value contradicts the premise
if runs_average_hypothesis <= runs_average_premise:
    label = "contradiction"
else:
    # The hypothesis value is greater than the premise, so the hypothesis cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
