second_leg_time_premise = 7
second_leg_time_hypothesis = 6

# the hypothesis talks about the time Henry runs the second leg of the course, referenced also in the premise
if second_leg_time_premise <= second_leg_time_hypothesis:
    # check if the hypothesis value contradicts the estimate of more than'second_leg_time_hypothesis'
    label = "contradiction"
else:
    # the premise gives the exact time Henry runs the second leg of the course
    # any time greater than'second_leg_time_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
