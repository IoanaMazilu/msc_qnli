speed_premise = 60
speed_hypothesis = 50

# the hypothesis refers to the speed at which Tom drives, which is also mentioned in the premise
if speed_premise <= speed_hypothesis:
    # check if the speed in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the speed in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
