# Premise: One hour after Yolanda started walking from X to Y, a distance of 24 miles, Bob started walking along the same road from Y to X.
# Hypothesis: One hour after Yolanda started walking from X to Y, a distance of 64 miles, Bob started walking along the same road from Y to X.
# Golden Label: contradiction

distance_premise = 24
distance_hypothesis = 64

# the hypothesis talks about the distance between X and Y, referenced also in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the distance in the premise, we can infer entailment
    label = "entailment"

print(label)

