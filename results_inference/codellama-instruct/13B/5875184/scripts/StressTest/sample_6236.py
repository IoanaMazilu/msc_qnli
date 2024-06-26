premise_speed = 10
premise_time = 3
hypothesis_speed = 20
hypothesis_time = 1.5

# the hypothesis refers to the time it would take to clean the house with doubled speed
if hypothesis_time < premise_time:
    # check if the estimate of 'hypothesis_time' contradicts the time mentioned in the premise
    label = "contradiction"
elif hypothesis_speed!= premise_speed:
    # check if the speed mentioned in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
