# Define variables for numerical entities in the premise and hypothesis
maxwell_walking_speed_premise = 4
brad_running_speed_premise = 6
distance_premise = 40

# Define variables for numerical entities in the hypothesis
maxwell_walking_speed_hypothesis = 4
brad_running_speed_hypothesis = 6
distance_hypothesis = 80

# Calculate the distance traveled by Brad based on the hypothesis
brad_distance_hypothesis = distance_hypothesis * brad_running_speed_hypothesis / (brad_running_speed_hypothesis + maxwell_walking_speed_hypothesis)

# Compare the distance traveled by Brad in the premise and hypothesis
if brad_distance_premise == brad_distance_hypothesis:
    # If the distance traveled by Brad is the same in both the premise and hypothesis, we can infer entailment
    label = "entailment"
elif brad_distance_premise < brad_distance_hypothesis:
    # If the distance traveled by Brad in the hypothesis is greater than in the premise, we can infer contradiction
    label = "contradiction"
else:
    # If the distance traveled by Brad in the hypothesis is less than or equal to in the premise, we can infer neutrality
    label = "neutral"

print(label)
