jog_speed_premise = 4
jog_speed_hypothesis = 3
walk_speed_premise = 6
walk_speed_hypothesis = 6

# the hypothesis refers to the jog and walk speeds mentioned in the premise
if jog_speed_hypothesis >= jog_speed_premise:
    # check if the jog speed in the hypothesis contradicts the estimate of less than 'jog_speed_premise'
    label = "contradiction"
elif walk_speed_hypothesis!= walk_speed_premise:
    # check if the walk speed in the hypothesis contradicts the walk speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
