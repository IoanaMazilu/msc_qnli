ratio_premise = 2/3
ratio_hypothesis = 4/3

# the hypothesis refers to the ratio of distances between A to B and B to C mentioned in the premise
if ratio_premise >= ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
elif ratio_premise == ratio_hypothesis:
    # check if the ratio in the hypothesis is equal to the ratio mentioned in the premise
    label = "entailment"
else:
    # if the hypothesis does not contradict the premise and cannot be fully entailed from the premise
    label = "neutral"

print(label)
