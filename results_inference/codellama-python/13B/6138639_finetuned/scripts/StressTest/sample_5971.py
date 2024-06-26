leg_time_premise = 6
leg_time_hypothesis = 7

# the hypothesis talks about the time Henry runs the second leg of the course, referenced also in the premise
if leg_time_hypothesis <= leg_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'leg_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the leg time
    # any leg time greater than 'leg_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
