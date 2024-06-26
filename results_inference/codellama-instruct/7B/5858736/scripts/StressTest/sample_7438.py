# Define variables for the numerical entities in the premise and hypothesis
racetrack_horses_premise = 25
racetrack_horses_hypothesis = 3

# Extract the quantities as valid numbers
racetrack_horses_premise = int(racetrack_horses_premise)
racetrack_horses_hypothesis = int(racetrack_horses_hypothesis)

# Check if the hypothesis value contradicts the premise
if racetrack_horses_hypothesis > racetrack_horses_premise:
    # The hypothesis value contradicts the premise, so the label is "contradiction"
    label = "contradiction"
else:
    # The hypothesis value does not contradict the premise, so the label is "neutral"
    label = "neutral"

print(label)
