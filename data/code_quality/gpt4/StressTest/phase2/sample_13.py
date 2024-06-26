driving_speed_premise = 65
driving_speed_hypothesis = 85

# the hypothesis talks about the driving speed of John, mentioned also in the premise
if driving_speed_hypothesis <= driving_speed_premise:
    # check if the hypothesis value contradicts the premise estimate of more than 'driving_speed_premise'
    label = "contradiction"
else:
    # the premise gives only a lower bound for the driving speed
    # any driving speed greater than 'driving_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
