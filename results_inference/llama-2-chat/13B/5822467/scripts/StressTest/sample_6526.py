flights_departed_premise = 3
flights_departed_hypothesis = 3
on_time_departure_rate_premise = 20
on_time_departure_rate_hypothesis = 60

# the hypothesis refers to the number of on-time departures needed for a certain on-time departure rate
if flights_departed_hypothesis <= on_time_departure_rate_premise:
    # check if the estimate of 'on_time_departure_rate_hypothesis' contradicts the premise
    label = "contradiction"
elif flights_departed_hypothesis > on_time_departure_rate_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the on-time departure rate
    # any on-time departure rate greater than 'on_time_departure_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
