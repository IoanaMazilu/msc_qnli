next_flights_premise = 3
next_flights_hypothesis = 3
on_time_departure_rate_premise = 0.5
on_time_departure_rate_hypothesis = 0.1

# the hypothesis talks about the number of subsequent flights and the on-time departure rate, referenced also in the premise
if next_flights_hypothesis!= next_flights_premise:
    # check if the number of subsequent flights in the hypothesis contradicts the number of subsequent flights reported in the premise
    label = "contradiction"
elif on_time_departure_rate_hypothesis!= on_time_departure_rate_premise:
    # check if the on-time departure rate in the hypothesis contradicts the on-time departure rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
