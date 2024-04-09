next_flights_premise = 3
next_flights_hypothesis = 3

# the hypothesis talks about the number of on-time flights needed for the airport's on-time departure rate to be higher than 10%
if next_flights_hypothesis <= next_flights_premise:
    # check if the hypothesis value contradicts the estimate of 'next_flights_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of on-time flights, but the hypothesis provides a more specific estimate
    # any number of on-time flights greater than 'next_flights_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
