speed_premise = 30
speed_hypothesis = 60

# the hypothesis talks about the speed of two entities, referenced also in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of the speed of Bruce in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Bruce, any speed greater than 30 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
