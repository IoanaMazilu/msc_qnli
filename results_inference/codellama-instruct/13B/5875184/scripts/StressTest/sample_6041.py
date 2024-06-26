premise_speed = 90
premise_time = 12
hypothesis_speed = 90
hypothesis_time = 12

# the hypothesis refers to the speed and time mentioned in the premise
if hypothesis_speed <= premise_speed:
    # check if the estimate of 'hypothesis_speed' contradicts the speed in the premise
    label = "contradiction"
elif hypothesis_time!= premise_time:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
