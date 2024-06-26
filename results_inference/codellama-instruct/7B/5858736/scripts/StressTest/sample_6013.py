# Define variables for the premise and hypothesis
Karen_speed_premise = 20
Tom_speed_premise = 45
Karen_speed_hypothesis = 60
Tom_speed_hypothesis = 45

# Calculate the distance traveled by Karen and Tom
Karen_distance_premise = (Karen_speed_premise * 100) / 3600
Tom_distance_premise = (Tom_speed_premise * 100) / 3600
Karen_distance_hypothesis = (Karen_speed_hypothesis * 100) / 3600
Tom_distance_hypothesis = (Tom_speed_hypothesis * 100) / 3600

# Compare the distances traveled by Karen and Tom
if Karen_distance_hypothesis <= Karen_distance_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'Karen_distance_premise'
    label = "contradiction"
elif Tom_distance_hypothesis <= Tom_distance_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'Tom_distance_premise'
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
