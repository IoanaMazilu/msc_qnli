speed_premise = 40
speed_hypothesis = 70

# the hypothesis refers to the speed of Bob's driving from City A to City B, mentioned in the premise
if speed_premise >= speed_hypothesis:
    # check if the speed in the premise contradicts the estimate of less than'speed_hypothesis'
    label = "contradiction"
else:
    # if the premise speed does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
