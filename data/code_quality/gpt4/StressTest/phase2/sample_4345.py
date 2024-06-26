speed_premise = 20
speed_hypothesis = 40

# the hypothesis talks about the driving speed, also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the premise stating 'more than speed_premise'
    label = "contradiction"
else:
    # the premise gives only a lower limit for the speed
    # any speed greater than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
