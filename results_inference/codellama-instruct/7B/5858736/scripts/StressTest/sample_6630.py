# Define variables for the premise and hypothesis
distance_premise = 500
speed_premise = 15
time_premise = distance_premise / speed_premise

distance_hypothesis = 800
time_hypothesis = distance_hypothesis / speed_premise

# Check if the hypothesis contradicts the premise
if time_hypothesis > time_premise:
    label = "contradiction"
else:
    # If the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
