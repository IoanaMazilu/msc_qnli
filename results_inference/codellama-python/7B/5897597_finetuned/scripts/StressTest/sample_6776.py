ratio_premise = [4, 2]
ratio_hypothesis = [3, 2]

# the hypothesis refers to the ratio of distances between A to B and B to C mentioned in the premise
if ratio_premise!= ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
