distance_from_tripoli_premise = 50
distance_from_tripoli_hypothesis = 50

# the hypothesis mentions the distance from Tripoli where the four reporters were kidnapped, which is also mentioned in the premise
if distance_from_tripoli_hypothesis != distance_from_tripoli_premise:
    # check if the distance from Tripoli in the hypothesis contradicts the distance from Tripoli reported in the premise
    label = "contradiction"
else:
    # if the hypothesis distance does not contradict the premise distance, we can infer entailment
    label = "entailment"

print(label)
