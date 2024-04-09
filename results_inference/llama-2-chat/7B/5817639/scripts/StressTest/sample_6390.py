speed_premise = 6
speed_hypothesis = 1

# the hypothesis talks about the speed of Sacha and Bruno
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of Sacha's speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Sacha's speed
    # any speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
