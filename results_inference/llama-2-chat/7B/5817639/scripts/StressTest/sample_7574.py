speed_premise = 2
speed_hypothesis = 3

# the hypothesis talks about the speed of Fred and Sam, referenced also in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of the speed of Fred in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Fred
    # any speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
