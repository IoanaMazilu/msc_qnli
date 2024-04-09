# Variables to represent the quantities in the premise and hypothesis
gumballs_premise = 17 + 12 + X
gumballs_hypothesis = 57 + 12 + X

# Check if the hypothesis values contradict the premise values
if gumballs_hypothesis > gumballs_premise:
    # The hypothesis value contradicts the premise value, so label is contradiction
    label = "contradiction"
elif gumballs_hypothesis < gumballs_premise:
    # The premise value is greater than the hypothesis value, so label is entailment
    label = "entailment"
else:
    # If the hypothesis values are consistent with the premise values, label is neutral
    label = "neutral"

print(label)
