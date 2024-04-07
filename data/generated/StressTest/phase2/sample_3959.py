# Premise: Lionel left his house and walked towards Walt's house, 48 miles away.
# Hypothesis: Lionel left his house and walked towards Walt's house, 18 miles away.
# Golden Label: contradiction

distance_to_walt_premise = 48
distance_to_walt_hypothesis = 18

# the hypothesis and premise both refer to the distance from Lionel's house to Walt's house
if distance_to_walt_hypothesis != distance_to_walt_premise:
    # check if the distance in the hypothesis contradicts the distance stated in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

