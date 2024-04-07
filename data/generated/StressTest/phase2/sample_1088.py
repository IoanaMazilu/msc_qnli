# Premise: One hour after Matthew started waking from q to y, a distance of 45 km, Johnny started walking along the same road from y to q.
# Hypothesis: One hour after Matthew started waking from q to y, a distance of 55 km, Johnny started walking along the same road from y to q.
# Golden Label: contradiction

distance_premise = 45
distance_hypothesis = 55

# the hypothesis refers to the same distance from q to y mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

