jog_speed_premise = 3
jog_speed_hypothesis = 5
walk_speed_premise = 10
walk_speed_hypothesis = 10

# the hypothesis provides specific speeds for Aaron's jogging and walking, also referenced in the premise
if jog_speed_hypothesis <= jog_speed_premise:
    # check if the hypothesis value contradicts the premise estimate of more than 'jog_speed_premise'
    label = "contradiction"
elif walk_speed_hypothesis != walk_speed_premise:
    # check if the walking speed in the hypothesis contradicts the walking speed mentioned in the premise
    label = "contradiction"
else:
    # the premise only gives an estimate for the jogging speed
    # a jogging speed greater than 'jog_speed_premise' does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
