ramesh_premise = 2/1
ramesh_hypothesis = 6/1

# the hypothesis refers to the ratio for Ramesh mentioned in the premise
if ramesh_hypothesis <= ramesh_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
