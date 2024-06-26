# Define variables for the premise and hypothesis
premise_speed = 5
hypothesis_speed = 8

# Calculate the distance traveled by Fred and Sam
distance_premise = premise_speed * 5
distance_hypothesis = hypothesis_speed * 5

# Check if the hypothesis contradicts the premise
if distance_hypothesis > distance_premise:
    label = "contradiction"
else:
    # The hypothesis does not contradict the premise, but it cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
