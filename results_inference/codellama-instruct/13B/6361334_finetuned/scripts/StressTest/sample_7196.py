distance_premise = 7
distance_hypothesis = 7
time_premise = 1
time_hypothesis = 1

# the hypothesis refers to the time required to cover the distance between Chennai and Jammu, mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the number of days and minutes in the premise
    label = "contradiction"
elif time_hypothesis!= time_premise:
    # check if the number of minutes in the hypothesis contradicts the number of minutes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
