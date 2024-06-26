chairs_premise = 6
chairs_hypothesis = 4

# both the premise and hypothesis mention the number of chairs
if chairs_premise != chairs_hypothesis:
    # check if the number of chairs in the hypothesis contradicts the number of chairs reported in the premise
    label = "contradiction"
else:
    # in this case, the number of chairs in the hypothesis matches the number in the premise, so the relation is entailment
    label = "entailment"

print(label)
