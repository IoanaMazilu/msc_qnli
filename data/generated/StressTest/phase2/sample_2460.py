# Premise: Jack wants to take 5 apples.
# Hypothesis: Jack wants to take more than 3 apples.
# Golden Label: entailment

apples_premise = 5
apples_hypothesis = 3

# the hypothesis refers to the number of apples Jack wants to take, mentioned in the premise
if apples_premise <= apples_hypothesis:
    # check if the number of apples Jack wants to take in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)

