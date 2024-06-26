distance_walked_premise = 31
distance_walked_hypothesis = 61

# The hypothesis talks about the distance from X to Y, which is also mentioned in the premise
if distance_walked_premise != distance_walked_hypothesis:
    # Check if the distance in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # If the distance in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
