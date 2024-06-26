# Define variables for the premise and hypothesis
Karen_speed_premise = 80
Tom_speed_premise = 45
Karen_speed_hypothesis = 60
Tom_speed_hypothesis = 45

# Calculate the distance that Tom will drive before Karen wins the bet
Tom_distance_premise = (Karen_speed_premise - Tom_speed_premise) * Q
Tom_distance_hypothesis = (Karen_speed_hypothesis - Tom_speed_hypothesis) * Q

# Check if the hypothesis contradicts the premise
if Tom_distance_hypothesis <= Tom_distance_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
