ratio_lewis_brown_premise = 1/2
ratio_lewis_brown_hypothesis = 6/2

# the hypothesis refers to the ratio of ages of Lewis and Brown mentioned in the premise
if ratio_lewis_brown_premise >= ratio_lewis_brown_hypothesis:
    # check if the ratio of 'ratio_lewis_brown_premise' contradicts the ratio in the hypothesis
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
