premise_on_time_flights = 3
hypothesis_on_time_flights = 3

# the hypothesis refers to the number of on-time flights mentioned in the premise
if hypothesis_on_time_flights <= premise_on_time_flights:
    # check if the estimate of 'hypothesis_on_time_flights' contradicts the number of on-time flights in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of on-time flights
    # any number of on-time flights greater than 'premise_on_time_flights' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
