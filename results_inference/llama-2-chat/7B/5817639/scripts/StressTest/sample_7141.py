next_flight_departure_premise = 0
next_flight_departure_hypothesis = 3

# the hypothesis talks about the number of subsequent flights that need to depart on-time from Phoenix
if next_flight_departure_hypothesis <= next_flight_departure_premise:
    # check if the hypothesis value contradicts the estimate of 'next_flight_departure_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of subsequent flights that need to depart on-time
    # any number of subsequent flights that need to depart on-time greater than 'next_flight_departure_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
