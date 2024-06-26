seconds_premise = 500
speed_premise = 15
speed_hypothesis = 15

# the hypothesis talks about the time taken to cover a distance greater than 500 meters
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of less than'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
