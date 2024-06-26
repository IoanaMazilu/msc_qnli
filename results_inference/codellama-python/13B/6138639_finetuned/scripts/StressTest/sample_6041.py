speed_premise = 90
speed_hypothesis = 90
speed_increase = 20

# the hypothesis refers to the speed of Xavier mentioned in the premise
if speed_premise <= speed_hypothesis:
    # check if the estimate of'speed_hypothesis' contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
