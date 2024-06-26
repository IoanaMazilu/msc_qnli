# Define variables for the premise and hypothesis
speed_premise = 30
speed_hypothesis = 50

# Check if the hypothesis speed is less than the premise speed
if speed_hypothesis < speed_premise:
    # The hypothesis contradicts the premise, so the label is "contradiction"
    label = "contradiction"
else:
    # The hypothesis does not contradict the premise, so the label is "neutral"
    label = "neutral"

print(label)
