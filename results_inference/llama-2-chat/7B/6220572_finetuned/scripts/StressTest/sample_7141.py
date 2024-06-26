flight_departure_rate_premise = 40
flight_departure_rate_hypothesis = 50

# the hypothesis refers to the on-time departure rate of flights from Phoenix, also mentioned in the premise
if flight_departure_rate_hypothesis <= flight_departure_rate_premise:
    # check if the hypothesis estimate contradicts the premise estimate
    label = "contradiction"
else:
    # the premise gives only an estimate for the on-time departure rate
    # any on-time departure rate greater than 'flight_departure_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
