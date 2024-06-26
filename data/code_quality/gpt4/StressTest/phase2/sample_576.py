speed_premise = 40
speed_hypothesis = 70

# the hypothesis refers to the speed at which Bob is driving, mentioned also in the premise
if speed_hypothesis <= speed_premise:
    # check if the estimate of 'speed_hypothesis' contradicts the speed reported in the premise
    label = "contradiction"
elif speed_premise != speed_hypothesis:
    # check if the speed in the hypothesis is the same as the speed reported in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
