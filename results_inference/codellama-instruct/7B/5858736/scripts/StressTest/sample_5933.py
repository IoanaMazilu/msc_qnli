# Define variables for the premise and hypothesis
herd_parts_premise = 5
herd_parts_hypothesis = 6

# Check if the hypothesis contradicts the premise
if herd_parts_hypothesis > herd_parts_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
