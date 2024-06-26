premise_speed_karen = 60
premise_speed_tom = 45
hypothesis_speed_karen = 80
hypothesis_speed_tom = 45

# the hypothesis refers to the average speed of Karen and Tom, mentioned in the premise
if hypothesis_speed_karen < premise_speed_karen:
    # check if the estimate of 'hypothesis_speed_karen' contradicts the average speed of Karen in the premise
    label = "contradiction"
elif hypothesis_speed_tom!= premise_speed_tom:
    # check if the average speed of Tom in the hypothesis contradicts the average speed of Tom reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
