jog_speed_premise = 4
jog_speed_hypothesis = 4
walk_speed_premise = 8
walk_speed_hypothesis = 8

# the hypothesis refers to the jogging and walking speeds mentioned in the premise
if jog_speed_hypothesis >= jog_speed_premise:
    # check if the hypothesis value contradicts the jogging speed in the premise
    label = "contradiction"
elif walk_speed_hypothesis!= walk_speed_premise:
    # check if the walking speed in the hypothesis contradicts the walking speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
