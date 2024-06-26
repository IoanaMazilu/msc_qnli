flights_departed_premise = 3
flights_departed_hypothesis = 3
on_time_departure_rate_premise = 0.8
on_time_departure_rate_hypothesis = 0.7

# the hypothesis refers to the on-time departure rate of the airport, which is also mentioned in the premise
if on_time_departure_rate_hypothesis >= on_time_departure_rate_premise:
    # check if the hypothesis value contradicts the on-time departure rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the on-time departure rate
    # any on-time departure rate lower than 'on_time_departure_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
