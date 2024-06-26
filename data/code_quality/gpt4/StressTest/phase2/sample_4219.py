jog_speed_premise = 4
jog_speed_hypothesis = 6
walk_speed_premise = 12
walk_speed_hypothesis = 12

# the hypothesis refers to the speed at which Aaron will jog and walk, also mentioned in the premise
if jog_speed_hypothesis <= jog_speed_premise:
    # check if the jogging speed in the hypothesis contradicts the estimate of more than 'jog_speed_premise'
    label = "contradiction"
elif walk_speed_hypothesis != walk_speed_premise:
    # check if the walking speed in the hypothesis contradicts the walking speed mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the jogging speed
    # a jogging speed greater than 'jog_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
