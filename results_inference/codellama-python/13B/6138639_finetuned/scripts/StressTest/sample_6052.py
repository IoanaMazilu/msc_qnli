jog_speed_premise = 4
jog_speed_hypothesis = 3
walk_speed_premise = 6
walk_speed_hypothesis = 6

# the hypothesis talks about the speed of jogging and walking, referenced also in the premise
if jog_speed_hypothesis >= jog_speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'jog_speed_premise'
    label = "contradiction"
elif walk_speed_hypothesis!= walk_speed_premise:
    # check if the speed of walking in the hypothesis contradicts the speed of walking reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of jogging
    # any speed of jogging less than 'jog_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
