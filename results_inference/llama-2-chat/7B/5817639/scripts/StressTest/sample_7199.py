# Define variables for the premise and hypothesis
side_premise = 3
side_hypothesis = 7

# Check if the hypothesis values contradict the premise values
if side_hypothesis <= side_premise:
    label = "contradiction"
else:
    # The hypothesis values exceed the premise values, but do not contradict them
    label = "neutral"

print(label)
