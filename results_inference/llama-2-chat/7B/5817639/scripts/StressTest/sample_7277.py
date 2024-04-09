molly_speed_premise = 100
molly_speed_hypothesis = 100

# the hypothesis talks about the speed of Molly and Max, which is also referred to in the premise
if molly_speed_hypothesis <= molly_speed_premise:
    # check if the hypothesis value contradicts the estimate of'molly_speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Molly and Max
    # any speed lower than'molly_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
