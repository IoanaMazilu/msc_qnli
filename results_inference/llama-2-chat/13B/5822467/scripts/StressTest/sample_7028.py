# Define variables for the numerical entities in the premise and hypothesis
cara_leaves_premise = 120
dan_leaves_hypothesis = 120

# Check if the hypothesis value contradicts the premise value
if dan_leaves_hypothesis > cara_leaves_premise:
    # The hypothesis value contradicts the premise value, so the label is contradiction
    label = "contradiction"
elif dan_leaves_hypothesis == cara_leaves_premise:
    # The hypothesis value is equal to the premise value, so the label is neutral
    label = "neutral"
else:
    # The hypothesis value is less than the premise value, so the label is entailment
    label = "entailment"

print(label)
