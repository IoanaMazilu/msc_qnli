speed_premise = 40
speed_hypothesis = 70

# the hypothesis refers to the speed at which Bob drives, mentioned in the premise
if speed_premise >= speed_hypothesis:
    # check if the speed in the premise contradicts the estimate of less than'speed_hypothesis'
    label = "contradiction"
elif speed_premise < speed_hypothesis:
    # if the speed in the premise is less than the estimate in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the speed in the premise is equal to the estimate in the hypothesis, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
