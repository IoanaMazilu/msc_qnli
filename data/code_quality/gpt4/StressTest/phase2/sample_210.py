speed_premise = 60
speed_hypothesis = 40

# the hypothesis refers to the speed of Tom's drive from town A to town B, mentioned in the premise
if speed_premise <= speed_hypothesis:
    # check if the estimate of 'speed_hypothesis' contradicts the speed of drive in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
