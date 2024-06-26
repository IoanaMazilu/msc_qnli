speed_premise = 40
speed_hypothesis = 60

# the hypothesis talks about the speed at which Tom drives, which is also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the speed in the hypothesis contradicts the estimate of more than 'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
