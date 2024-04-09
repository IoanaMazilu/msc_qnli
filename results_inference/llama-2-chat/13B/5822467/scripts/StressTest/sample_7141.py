flights_premise = 3
flights_hypothesis = 3
on_time_rate_premise = 40
on_time_rate_hypothesis = 50

# the hypothesis refers to the number of on-time flights needed for a certain on-time departure rate
if flights_hypothesis <= on_time_rate_premise:
    # check if the estimate of 'on_time_rate_hypothesis' contradicts the number of on-time flights in the premise
    label = "contradiction"
elif flights_hypothesis > on_time_rate_premise:
    # check if the number of on-time flights needed in the hypothesis exceeds the number of on-time flights in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
