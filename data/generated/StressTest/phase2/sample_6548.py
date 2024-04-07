# Premise: The distance between West-Town to East-Town is 15 kilometers.
# Hypothesis: The distance between West-Town to East-Town is more than 15 kilometers.
# Golden Label: contradiction

distance_premise = 15
distance_hypothesis = 15

# the hypothesis talks about the distance between two towns, mentioned also in the premise
if distance_hypothesis != distance_premise:
    # check if the hypothesis value contradicts the exact distance given in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

