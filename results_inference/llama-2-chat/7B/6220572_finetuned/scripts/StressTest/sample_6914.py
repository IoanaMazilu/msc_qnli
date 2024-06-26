three_flights_premise = 3
three_flights_hypothesis = 3
on_time_departure_rate_premise = 70
on_time_departure_rate_hypothesis = 50

# the hypothesis refers to the number of flights and the on-time departure rate mentioned in the premise
if three_flights_hypothesis!= three_flights_premise:
    # check if the number of flights in the hypothesis contradicts the number of flights reported in the premise
    label = "contradiction"
elif on_time_departure_rate_hypothesis >= on_time_departure_rate_premise:
    # check if the estimate of on-time departure rate in the hypothesis contradicts the on-time departure rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
