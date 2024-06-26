annie_speed_premise = 55
sam_speed_premise = 12
annie_speed_hypothesis = 15
sam_speed_hypothesis = 12

# the hypothesis refers to the speed of Annie and Sam mentioned in the premise
if annie_speed_hypothesis >= annie_speed_premise:
    # check if Annie's speed in the hypothesis contradicts the premise
    label = "contradiction"
elif sam_speed_hypothesis != sam_speed_premise:
    # check if Sam's speed contradicts the premise
    label = "contradiction"
elif annie_speed_hypothesis < annie_speed_premise and sam_speed_hypothesis == sam_speed_premise:
    # if the speeds in the hypothesis are consistent with the premise, we can infer entailment
    label = "entailment"

print(label)
