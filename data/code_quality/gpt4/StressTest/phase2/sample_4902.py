jog_speed_premise = 5
jog_speed_hypothesis = 3
walk_speed_premise = 10
walk_speed_hypothesis = 10

# the hypothesis refers to the speed of jogging and walking mentioned in the premise
if jog_speed_premise <= jog_speed_hypothesis:
    # check if the estimate of 'jog_speed_hypothesis' contradicts the jogging speed in the premise
    label = "contradiction"
elif walk_speed_hypothesis != walk_speed_premise:
    # check if the walking speed in the hypothesis contradicts the walking speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
