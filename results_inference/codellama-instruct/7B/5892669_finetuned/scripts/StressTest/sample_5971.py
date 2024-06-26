second_leg_time_premise = 6
second_leg_time_hypothesis = 7

# the hypothesis talks about the time Henry took to run the second leg of the course, referenced also in the premise
if second_leg_time_hypothesis <= second_leg_time_premise:
    # check if the hypothesis value contradicts the estimate of more than'second_leg_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Henry took
    # any time greater than'second_leg_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
