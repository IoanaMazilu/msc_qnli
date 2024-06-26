# Define variables for the numerical entities in the premise and hypothesis
kilometers_premise = 25.0
kilometers_per_hour_premise = 5.0
time_premise = 4.0

# Define variables for the numerical entities in the hypothesis
hours_hypothesis = 4.0
kilometers_hypothesis =?

# Calculate the total distance jogged in the premise
total_distance_premise = kilometers_premise * time_premise

# Calculate the total distance jogged in the hypothesis
total_distance_hypothesis = hours_hypothesis * kilometers_per_hour_premise

# Check if the total distance jogged in the hypothesis contradicts the estimate from the premise
if total_distance_hypothesis!= total_distance_premise:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
