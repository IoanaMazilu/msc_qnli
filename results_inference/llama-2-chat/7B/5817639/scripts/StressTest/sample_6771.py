speed_premise = 40
speed_hypothesis = 50

# the hypothesis talks about the speed of Murali's journey, referenced also in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of the speed in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the speed, but the hypothesis value is consistent with it
    label = "neutral"

print(label)
