# Define variables for the distances between Fred and Sam
distance_Fred_Sam_premise = 800
distance_Fred_Sam_hypothesis = 100

# Check if the distance between Fred and Sam in the hypothesis contradicts the distance reported in the premise
if distance_Fred_Sam_hypothesis <= distance_Fred_Sam_premise:
    label = "contradiction"
else:
    # The hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
