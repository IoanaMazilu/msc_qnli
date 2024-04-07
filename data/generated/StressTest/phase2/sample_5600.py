# Premise: Lionel left his house and walked towards Walt's house, 48 miles away.
# Hypothesis: Lionel left his house and walked towards Walt's house, more than 48 miles away.
# Golden Label: contradiction

distance_premise = 48
distance_hypothesis = 48

# the hypothesis refers to the distance of Walt's house mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

