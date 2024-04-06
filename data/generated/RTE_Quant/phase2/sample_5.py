# Premise: Scott Island is a small uninhabited island of volcanic origin in the Southern Ocean, 505 km northeastward of Cape Adare, the northeastern extremity of Victoria Land.
# Hypothesis: Scott Island lies 505 km northeastward of Victoria.
# Golden Label: neutral

distance_premise = 505
distance_hypothesis = 505

# the hypothesis talks about the distance from Scott Island to Victoria, which is also mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance from the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the distance in the premise, we can infer entailment
    label = "entailment"

print(label)

