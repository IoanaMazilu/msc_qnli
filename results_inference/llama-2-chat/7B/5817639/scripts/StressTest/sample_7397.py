speed_premise = 60
speed_hypothesis = 70

# the hypothesis talks about the speed of driving, which is also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis speed estimate contradicts the speed reported in the premise
    label = "contradiction"
else:
    # the premise provides an estimate for the speed, but the hypothesis speed value does not contradict it
    label = "entailment"

print(label)
