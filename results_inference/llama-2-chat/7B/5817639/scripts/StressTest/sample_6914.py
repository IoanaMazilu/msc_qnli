next_flights_premise = 3
next_flights_hypothesis = 3

# the hypothesis talks about the number of subsequent flights that need to depart from Phoenix on-time
if next_flights_hypothesis <= next_flights_premise:
    # check if the hypothesis value contradicts the estimate of 'next_flights_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of subsequent flights
    # any number of subsequent flights greater than 'next_flights_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
