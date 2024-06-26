# Define variables for the premise and hypothesis
premise_speed_f = 8
premise_speed_s = 5
hypothesis_speed_f = 5
hypothesis_speed_s = 5

# Calculate the distance traveled by Fred and Sam
distance_f = premise_speed_f * time
distance_s = hypothesis_speed_s * time

# Check if the hypothesis values contradict the premise
if distance_f!= distance_s:
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
