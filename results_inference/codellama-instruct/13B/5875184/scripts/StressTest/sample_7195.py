premise_time = 6
premise_minutes = 1
hypothesis_time = 7
hypothesis_minutes = 1

# the hypothesis refers to the time required by a train to cover the distance between Chennai and Jammu
if hypothesis_time > premise_time:
    # check if the estimate of 'hypothesis_time' contradicts the estimate of more than 'premise_time'
    label = "contradiction"
elif hypothesis_minutes!= premise_minutes:
    # check if the number of minutes in the hypothesis contradicts the number of minutes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
