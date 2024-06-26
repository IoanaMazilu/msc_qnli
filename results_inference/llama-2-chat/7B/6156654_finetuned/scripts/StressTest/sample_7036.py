# Define the premise and hypothesis
speed_premise = 5
speed_hypothesis = 5
distance_premise = 8
distance_hypothesis = 8

# Check if the hypothesis refers to the same situation as the premise
if speed_hypothesis!= speed_premise:
    # If the speeds in the hypothesis are different from the speeds in the premise, the hypothesis contradicts the premise
    label = "contradiction"
elif distance_hypothesis!= distance_premise:
    # If the distances in the hypothesis are different from the distances in the premise, the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis refers to the same situation as the premise, we can infer entailment
    label = "entailment"

print(label)
