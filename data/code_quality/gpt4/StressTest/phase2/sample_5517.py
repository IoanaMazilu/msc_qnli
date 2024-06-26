speed_b_premise = 40
speed_b_hypothesis = 10

# the hypothesis talks about the speed of B, that is also referenced in the premise
if speed_b_premise <= speed_b_hypothesis:
    # check if the speed of B in the premise contradicts the estimate of more than 'speed_b_hypothesis' in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
