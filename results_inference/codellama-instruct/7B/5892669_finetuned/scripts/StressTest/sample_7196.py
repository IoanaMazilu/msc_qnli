time_premise = 7
time_hypothesis = 7

# the hypothesis refers to the time required by a train to cover the distance between Chennai and Jammu mentioned in the premise
if time_hypothesis <= time_premise:
    # check if the estimate of 'time_hypothesis' contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
