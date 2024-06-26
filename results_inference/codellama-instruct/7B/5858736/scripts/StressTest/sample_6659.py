# Define variables for the premise and hypothesis
Karen_speed_premise = 60
Tom_speed_premise = 45
Karen_speed_hypothesis = 70
Tom_speed_hypothesis = 45

# Calculate the number of miles Tom will drive before Karen wins the bet
Tom_miles_premise = Karen_speed_premise * Q
Tom_miles_hypothesis = Karen_speed_hypothesis * Q

# Check if the hypothesis contradicts the premise
if Tom_miles_hypothesis <= Tom_miles_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
