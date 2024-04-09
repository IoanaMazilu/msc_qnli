speed_premise = 30
speed_hypothesis = 20

# the hypothesis talks about a higher constant speed than the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the constant speed
    # any constant speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
