premise_jog_speed = 4
premise_walk_speed = 8
hypothesis_jog_speed = 3
hypothesis_walk_speed = 8

# the hypothesis refers to the jog speed and walk speed mentioned in the premise
if hypothesis_jog_speed >= premise_jog_speed:
    # check if the estimate of 'hypothesis_jog_speed' contradicts the jog speed in the premise
    label = "contradiction"
elif hypothesis_walk_speed!= premise_walk_speed:
    # check if the walk speed in the hypothesis contradicts the walk speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
