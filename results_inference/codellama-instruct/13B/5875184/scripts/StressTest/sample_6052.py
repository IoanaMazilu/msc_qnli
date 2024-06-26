premise_speed_jogging = 4
premise_speed_walking = 6
hypothesis_speed_jogging = 3
hypothesis_speed_walking = 6

# the hypothesis refers to the speed of jogging and walking mentioned in the premise
if hypothesis_speed_jogging < premise_speed_jogging:
    # check if the estimate of 'hypothesis_speed_jogging' contradicts the speed of jogging in the premise
    label = "contradiction"
elif hypothesis_speed_walking!= premise_speed_walking:
    # check if the speed of walking in the hypothesis contradicts the speed of walking reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
