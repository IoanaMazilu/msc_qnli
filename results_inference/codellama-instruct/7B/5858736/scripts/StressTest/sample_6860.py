# Define variables for the premise and hypothesis
walk_distance_premise = 4
walk_time_premise = 1.25
walk_rate_premise = walk_distance_premise / walk_time_premise

# Define variables for the hypothesis
walk_distance_hypothesis = 4
walk_time_hypothesis = 1.25
walk_rate_hypothesis = walk_distance_hypothesis / walk_time_hypothesis

# Check if the hypothesis contradicts the premise
if walk_rate_hypothesis > walk_rate_premise:
    label = "contradiction"
else:
    # The hypothesis does not contradict the premise, but it cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
