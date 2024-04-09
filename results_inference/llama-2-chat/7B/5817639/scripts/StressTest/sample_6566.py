speed_premise = 80
speed_hypothesis = 60

# the hypothesis talks about the average speed for the trip, which is also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of the average speed in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the average speed, and any lower value than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
