fred_speed_premise = 6
sam_speed_premise = 5

fred_speed_hypothesis = 2
sam_speed_hypothesis = 5

# the hypothesis refers to the walking speeds of Fred and Sam mentioned in the premise
if fred_speed_premise != fred_speed_hypothesis:
    # check if Fred's speed in the hypothesis contradicts the value given in the premise
    label = "contradiction"
elif sam_speed_premise != sam_speed_hypothesis:
    # check if Sam's speed in the hypothesis contradicts the value given in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the speeds in the premise, we can infer entailment
    label = "entailment"

print(label)
