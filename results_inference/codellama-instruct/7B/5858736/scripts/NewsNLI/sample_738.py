# Define variables for the premise and hypothesis
distance_premise = 156
distance_hypothesis = 35

# Extract the numerical information from the premise and hypothesis
distance_premise = float(distance_premise)
distance_hypothesis = float(distance_hypothesis)

# Check if the hypothesis contradicts the premise
if distance_hypothesis!= distance_premise:
    # The hypothesis contradicts the premise, so the label is "contradiction"
    label = "contradiction"
else:
    # The hypothesis does not contradict the premise, so the label is "neutral"
    label = "neutral"

print(label)
