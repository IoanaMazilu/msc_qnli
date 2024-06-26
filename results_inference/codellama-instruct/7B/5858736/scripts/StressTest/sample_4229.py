# Define variables for the premise and hypothesis
speed_premise = 30
speed_hypothesis = 30

# Check if the hypothesis value contradicts the premise
if speed_hypothesis > speed_premise:
    label = "contradiction"
else:
    # The hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
