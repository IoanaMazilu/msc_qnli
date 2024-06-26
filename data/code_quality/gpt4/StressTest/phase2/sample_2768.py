annie_speed_premise = 15
sam_speed_premise = 12
annie_speed_hypothesis = 55
sam_speed_hypothesis = 12

# the hypothesis refers to the speed of Annie and Sam mentioned in the premise
if annie_speed_hypothesis != annie_speed_premise:
    # check if Annie's speed in the hypothesis contradicts her speed reported in the premise
    label = "contradiction"
elif sam_speed_hypothesis != sam_speed_premise:
    # check if Sam's speed in the hypothesis contradicts his speed reported in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the speeds in the premise, we can infer entailment
    label = "entailment"

print(label)
