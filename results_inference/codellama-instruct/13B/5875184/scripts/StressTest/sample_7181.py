premise_distance = 100
premise_time = 1
premise_speed = 42

hypothesis_distance = 100
hypothesis_time = 7
hypothesis_speed = 42

# the hypothesis refers to the same distance and time as the premise
if hypothesis_time <= premise_time:
    # check if the estimate of 'hypothesis_time' contradicts the time in the premise
    label = "contradiction"
elif hypothesis_speed!= premise_speed:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
