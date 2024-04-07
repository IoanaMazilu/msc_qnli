# Premise: One hour after Matthew started waking from r to y, a distance of 45 km, Johnny started walking along the same road from y to r.
# Hypothesis: One hour after Matthew started waking from r to y, a distance of more than 35 km, Johnny started walking along the same road from y to r.
# Golden Label: entailment

distance_ry_premise = 45
distance_ry_hypothesis = 35

# the hypothesis refers to the distance from r to y, mentioned also in the premise
if distance_ry_premise <= distance_ry_hypothesis:
    # check if the estimate of 'distance_ry_hypothesis' contradicts the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

