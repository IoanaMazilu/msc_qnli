# Define variables for the premise and hypothesis
right_premise = 62
left_premise = 4
right_hypothesis = 12
left_hypothesis = 4

# Calculate the difference between the premise and hypothesis
right_diff = right_hypothesis - right_premise
left_diff = left_hypothesis - left_premise

# Check if the difference between the premise and hypothesis is consistent with the hypothesis
if right_diff >= 0 and left_diff >= 0:
    # Check if the number of boys added to the line is consistent with the premise
    if right_diff + left_diff == 28:
        label = "entailment"
    else:
        label = "contradiction"
else:
    label = "neutral"

print(label)
