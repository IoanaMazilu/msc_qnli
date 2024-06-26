jog_speed_premise = 4
jog_speed_hypothesis = 3
walk_speed_premise = 6
walk_speed_hypothesis = 6

# the hypothesis refers to the speed of jogging and walking, mentioned in the premise
if jog_speed_hypothesis <= jog_speed_premise:
    # check if the estimate of 'jog_speed_hypothesis' contradicts the speed of jogging in the premise
    label = "contradiction"
elif walk_speed_hypothesis!= walk_speed_premise:
    # check if the speed of walking in the hypothesis contradicts the speed of walking reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
