speed_premise = 20
speed_hypothesis = 30

# the hypothesis talks about Ed's driving speed, which is also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the premise of more than'speed_premise'
    label = "contradiction"
else:
    # the premise provides an upper limit for the driving speed
    # any driving speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
