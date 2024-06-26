speed_premise = 25
speed_hypothesis = 35

# the hypothesis refers to the speed at which A starts from Delhi, mentioned in the premise
if speed_premise >= speed_hypothesis:
    # check if the speed in the premise contradicts the hypothesis statement of 'less than speed_hypothesis'
    label = "contradiction"
else:
    # if the premise speed does not contradict the hypothesis speed, we can infer entailment
    label = "entailment"

print(label)
