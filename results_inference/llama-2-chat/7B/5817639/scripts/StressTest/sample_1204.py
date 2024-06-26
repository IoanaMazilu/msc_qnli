speed_premise = 40
speed_hypothesis = 80

# the hypothesis talks about the average speed for the trip, which is also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of more than'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed,
    # any average speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
