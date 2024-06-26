# Define variables for the premise and hypothesis
distance_premise = 4
time_premise = 1.25
rate_premise = distance_premise / time_premise

distance_hypothesis = 3
time_hypothesis = 1.25
rate_hypothesis = distance_hypothesis / time_hypothesis

# Check if the hypothesis rate is greater than the premise rate
if rate_hypothesis > rate_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
