speed_premise = 5
speed_hypothesis = 8

# the hypothesis talks about the speed of Fred and Sam, which is also referred to in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of the speed of Fred and Sam in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Fred and Sam
    # any speed less than'speed_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
