premise_speed_karen = 20
premise_speed_tom = 45
hypothesis_speed_karen = 60
hypothesis_speed_tom = 45

# the hypothesis refers to the number of miles driven by Tom and Karen, as mentioned in the premise
if premise_speed_karen <= hypothesis_speed_karen:
    # check if the estimate of 'hypothesis_speed_karen' contradicts the number of miles driven by Karen in the premise
    label = "contradiction"
elif premise_speed_tom!= hypothesis_speed_tom:
    # check if the number of miles driven by Tom in the hypothesis contradicts the number of miles driven by Tom reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
