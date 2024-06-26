premise_flights_departed_ontime = 3
hypothesis_flights_departed_ontime = 3
premise_airport_ontime_departure_rate = 20
hypothesis_airport_ontime_departure_rate = 60

# the hypothesis refers to the number of flights departed on-time and the airport's on-time departure rate, both mentioned in the premise
if hypothesis_flights_departed_ontime!= premise_flights_departed_ontime:
    # check if the number of flights departed on-time in the hypothesis contradicts the number of flights departed on-time in the premise
    label = "contradiction"
elif hypothesis_airport_ontime_departure_rate <= premise_airport_ontime_departure_rate:
    # check if the airport's on-time departure rate in the hypothesis is lower than or equal to the on-time departure rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
