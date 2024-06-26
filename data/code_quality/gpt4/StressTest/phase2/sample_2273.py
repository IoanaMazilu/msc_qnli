ratio_premise = (2, 3)
ratio_hypothesis = (8, 3)

# the hypothesis refers to the ratio of distances between A to B and B to C mentioned in the premise
if ratio_premise != ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
