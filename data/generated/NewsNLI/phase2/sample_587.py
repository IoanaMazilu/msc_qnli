# Premise: Firefighters found the Boeing 737 on fire, with its wheels sheared off, resting in a ravine about 200 yards from the runway, Hynes said.
# Hypothesis: Jet also caught fire in ravine 200 yards from runway.
# Golden Label: neutral

distance_premise = 200
distance_hypothesis = 200

# the hypothesis mentions the distance to the runway, which is also mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the distance in the premise, we can infer entailment
    label = "entailment"

print(label)

