# Premise: One hour after Matthew started waking from r to y, a distance of 45 km, Johnny started walking along the same road from y to r.
# Hypothesis: One hour after Matthew started waking from r to y, a distance of 85 km, Johnny started walking along the same road from y to r.
# Golden Label: contradiction

distance_ry_premise = 45
distance_ry_hypothesis = 85

# the hypothesis refers to the distance between r and y mentioned in the premise
if distance_ry_hypothesis != distance_ry_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

