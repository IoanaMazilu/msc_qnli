premise_time = 44
premise_speed = 50
hypothesis_time = 24
hypothesis_speed = 50

# the hypothesis refers to the time taken by the bus to reach Pune
if hypothesis_time <= premise_time:
    # check if the estimate of 'hypothesis_time' contradicts the time taken by the bus in the premise
    label = "contradiction"
elif hypothesis_speed!= premise_speed:
    # check if the average speed of the bus in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
