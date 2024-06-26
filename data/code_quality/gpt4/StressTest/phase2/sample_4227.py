speed_premise = 30
speed_hypothesis = 10

# the hypothesis refers to the speed of Cara's driving between City A and City B, mentioned in the premise
if speed_premise < speed_hypothesis:
    # check if the speed in the premise contradicts the estimate of more than 'speed_hypothesis'
    label = "contradiction"
elif speed_premise == speed_hypothesis:
    # check if the speed in the premise contradicts the estimate of more than 'speed_hypothesis'
    label = "contradiction"
else:
    # if the speed in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"
    
print(label)
