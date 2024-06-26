# Define variables for the premise and hypothesis
distance_premise = 800
speed_premise = 15
time_premise = distance_premise / speed_premise

distance_hypothesis = 500
time_hypothesis = distance_hypothesis / speed_premise

# Check if the hypothesis contradicts the premise
if time_hypothesis > time_premise:
    label = "contradiction"
else:
    # The hypothesis does not contradict the premise, but it cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
