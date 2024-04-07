# Premise: One hour after Matthew started waking from q to y, a distance of 45 km, Johnny started walking along the same road from y to q.
# Hypothesis: One hour after Matthew started waking from q to y, a distance of more than 35 km, Johnny started walking along the same road from y to q.
# Golden Label: entailment

distance_premise = 45
distance_hypothesis = 35

# the hypothesis refers to the distance between 'q' and 'y' mentioned in the premise
if distance_premise <= distance_hypothesis:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

