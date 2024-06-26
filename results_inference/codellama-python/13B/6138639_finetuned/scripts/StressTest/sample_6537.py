speed_premise = 30
speed_hypothesis = 50

# the hypothesis refers to the speed of Cara's driving from City A to City B, mentioned in the premise
if speed_premise >= speed_hypothesis:
    # check if the speed in the premise contradicts the estimate of'speed_hypothesis'
    label = "contradiction"
else:
    # if the speed in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
