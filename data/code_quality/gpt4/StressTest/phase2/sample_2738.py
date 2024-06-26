distance_mohan_beats_premise = 104
distance_mohan_beats_hypothesis = 604

# the hypothesis refers to the same event as the premise, comparing the distances by which Mohan beats Rohan
if distance_mohan_beats_hypothesis != distance_mohan_beats_premise:
    # check if the distance by which Mohan beats Rohan in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
