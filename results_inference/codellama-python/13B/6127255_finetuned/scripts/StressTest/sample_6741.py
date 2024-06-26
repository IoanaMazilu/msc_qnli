speed_premise = 30
speed_hypothesis = 20

# the hypothesis refers to the speed Ed drives at, which is also mentioned in the premise
if speed_premise <= speed_hypothesis:
    # check if the speed in the premise contradicts the hypothesis that Ed drives at a speed more than'speed_hypothesis'
    label = "contradiction"
else:
    # if the speed in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
