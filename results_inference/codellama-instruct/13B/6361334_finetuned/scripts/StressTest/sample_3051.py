ride_time_premise = 3
ride_time_hypothesis = 1

# the hypothesis refers to the duration of the bike ride mentioned in the premise
if ride_time_hypothesis <= ride_time_premise:
    # check if the estimate of 'ride_time_hypothesis' contradicts the duration of the bike ride in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
