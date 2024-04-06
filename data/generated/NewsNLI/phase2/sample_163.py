# Premise: The three sailors were unharmed and are safely back aboard.
# Hypothesis: '' The three sailors were unharmed and are safely back aboard,'' spokesman says.
# Golden Label: entailment

sailors_premise = 3
sailors_hypothesis = 3

# the hypothesis mentions the number of sailors, which is also referenced in the premise
# the statement from the hypothesis is included in the premise, so there is no additional information or contradiction
if sailors_hypothesis != sailors_premise:
    # check if the number of sailors in the hypothesis contradicts the number of sailors stated in the premise
    label = "contradiction"
else:
    # if the number of sailors in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

