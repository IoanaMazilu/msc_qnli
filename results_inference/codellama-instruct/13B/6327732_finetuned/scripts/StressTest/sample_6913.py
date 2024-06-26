premise_flights = 3
hypothesis_flights = 70

# the hypothesis refers to the on-time departure rate of the airport
if hypothesis_flights <= premise_flights:
    # check if the hypothesis value contradicts the number of flights in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of flights
    # any number of flights greater than 'premise_flights' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
