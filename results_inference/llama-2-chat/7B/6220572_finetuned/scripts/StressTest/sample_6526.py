flight_departure_premise = 20
flight_departure_hypothesis = 60

# the hypothesis talks about the on-time departure rate of flights from Phoenix, referenced also in the premise
if flight_departure_hypothesis <= flight_departure_premise:
    # check if the hypothesis value contradicts the estimate of more than 'flight_departure_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the on-time departure rate
    # any on-time departure rate greater than 'flight_departure_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
