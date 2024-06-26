jog_speed_premise = 4
jog_speed_hypothesis = 4
walk_speed_premise = 8
walk_speed_hypothesis = 8

# the hypothesis talks about the speed of jogging and walking of Aaron, same as the premise
if jog_speed_premise != jog_speed_hypothesis:
    # check if the jogging speed in the hypothesis contradicts the jogging speed mentioned in the premise
    label = "contradiction"
elif walk_speed_premise != walk_speed_hypothesis:
    # check if the walking speed in the hypothesis contradicts the walking speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
