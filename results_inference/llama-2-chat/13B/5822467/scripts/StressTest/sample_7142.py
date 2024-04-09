flights_premise = 3
flights_hypothesis = 3
on_time_rate_premise = 50
on_time_rate_hypothesis = 10

# the hypothesis refers to the number of on-time flights needed for a certain on-time departure rate
if flights_hypothesis <= on_time_rate_premise / on_time_rate_hypothesis:
    # check if the estimate of 'on_time_rate_hypothesis' contradicts the premise
    label = "contradiction"
elif flights_premise!= flights_hypothesis:
    # check if the number of on-time flights in the hypothesis contradicts the number of on-time flights reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
