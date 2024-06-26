speed_premise = 9
speed_hypothesis = 10

# the hypothesis talks about the speed of two entities, referenced also in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of one entity
    # any speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
