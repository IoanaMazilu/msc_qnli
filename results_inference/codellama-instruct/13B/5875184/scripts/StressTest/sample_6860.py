premise_distance = 4
premise_time = 1.25
hypothesis_distance = 4
hypothesis_time = 1.25

# the hypothesis refers to the distance and time mentioned in the premise
if hypothesis_distance > premise_distance:
    # check if the estimate of 'hypothesis_distance' contradicts the distance in the premise
    label = "contradiction"
elif hypothesis_time > premise_time:
    # check if the estimate of 'hypothesis_time' contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
