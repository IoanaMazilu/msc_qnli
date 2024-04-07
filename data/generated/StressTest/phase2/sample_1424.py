# Premise: One hour after Yolanda started walking from X to Y, a distance of 52 miles, Bob started walking along the same road from Y to X.
# Hypothesis: One hour after Yolanda started walking from X to Y, a distance of 62 miles, Bob started walking along the same road from Y to X.
# Golden Label: contradiction

distance_premise = 52
distance_hypothesis = 62

# the hypothesis refers to the same distance that Yolanda and Bob are walking, mentioned in the premise
if distance_premise != distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis is the same as the one in the premise, we can infer entailment
    label = "entailment"

print(label)

