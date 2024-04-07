# Premise: A runner runs the 40 miles from Marathon to Athens at a constant speed.
# Hypothesis: A runner runs the 30 miles from Marathon to Athens at a constant speed.
# Golden Label: contradiction

distance_premise = 40
distance_hypothesis = 30

# the hypothesis talks about the distance from Marathon to Athens, referenced also in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the distance in the premise, we can infer entailment
    label = "entailment"

print(label)

