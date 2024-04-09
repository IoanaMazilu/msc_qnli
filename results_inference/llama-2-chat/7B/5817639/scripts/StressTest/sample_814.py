speed_premise = 30
speed_hypothesis = 40

# the hypothesis talks about the speed of Murali's journey, referenced also in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of more than'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Murali's journey
    # any speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
