# Premise: How many different ways can you arrange the 4 dancers in a line if Anne must be first or second.
# Hypothesis: How many different ways can you arrange the 3 dancers in a line if Anne must be first or second.
# Golden Label: contradiction

dancers_premise = 4
dancers_hypothesis = 3

# the hypothesis refers to the number of dancers mentioned in the premise
if dancers_hypothesis != dancers_premise:
    # check if the number of dancers in the hypothesis contradicts the number of dancers reported in the premise
    label = "contradiction"
else:
    # if the number of dancers in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

