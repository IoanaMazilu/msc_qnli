jog_speed_premise = 3
jog_speed_hypothesis = 7
walk_speed_premise = 6
walk_speed_hypothesis = 6

# the hypothesis refers to the jogging and walking speeds mentioned in the premise
if jog_speed_premise!= jog_speed_hypothesis:
    # check if the jogging speed in the hypothesis contradicts the jogging speed reported in the premise
    label = "contradiction"
elif walk_speed_hypothesis!= walk_speed_premise:
    # check if the walking speed in the hypothesis contradicts the walking speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
