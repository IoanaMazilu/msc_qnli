ratio_premise = [4, 3, 1]
ratio_hypothesis = [4, 3, 1]

# the hypothesis refers to the ratio of toy bricks used in building the tower, which is also mentioned in the premise
if ratio_hypothesis[0] >= ratio_premise[0] or ratio_hypothesis[1] >= ratio_premise[1] or ratio_hypothesis[2] >= ratio_premise[2]:
    # check if any of the ratios in the hypothesis contradicts the ratios in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
