# Define variables for the premise and hypothesis
friends_premise = 6
combinations_premise = 4

# Define variables for the hypothesis
more_than_4_hypothesis = 6

# Check if the hypothesis value contradicts the premise value
if more_than_4_hypothesis <= combinations_premise:
    # The hypothesis value contradicts the premise value, so label is contradiction
    label = "contradiction"
elif more_than_4_hypothesis > combinations_premise:
    # The hypothesis value is greater than the premise value, so label is entailment
    label = "entailment"
else:
    # The hypothesis value is consistent with the premise value, so label is neutral
    label = "neutral"

print(label)
