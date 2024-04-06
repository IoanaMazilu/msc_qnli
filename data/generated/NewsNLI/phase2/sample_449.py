# Premise: Sheriff:Suzanne Hopper, who was killed, was married and the mother of two children.
# Hypothesis: He said she was married and the mother of two children.
# Golden Label: entailment

children_premise = 2
children_hypothesis = 2

# the hypothesis mentions the marital status and the number of children of Suzanne Hopper, which are also mentioned in the premise
if children_hypothesis != children_premise:
    # check if the number of children in the hypothesis contradicts the number of children mentioned in the premise
    label = "contradiction"
else:
    # if the number of children in the hypothesis does not contradict the number of children in the premise, we can infer entailment
    label = "entailment"

print(label)

