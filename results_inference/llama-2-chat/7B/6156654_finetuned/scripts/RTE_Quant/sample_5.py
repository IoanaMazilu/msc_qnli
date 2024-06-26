distance_premise = 505
distance_hypothesis = 505

# the hypothesis mentions the distance from Scott Island to Victoria, which is also mentioned in the premise
if distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the distances match, it's an entailment
    label = "entailment"

print(label)
