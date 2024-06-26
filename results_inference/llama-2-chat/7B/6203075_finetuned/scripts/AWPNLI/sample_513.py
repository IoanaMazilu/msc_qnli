miles_flight_premise = 256.0
flights_premise = 32.0
miles_flight_hypothesis = 8191.0

# the hypothesis refers to the total miles flown, which is also mentioned in the premise
# compute the total miles flown in the premise
total_miles_flight_premise = miles_flight_premise * flights_premise

if miles_flight_hypothesis!= total_miles_flight_premise:
    # check if the total miles flown in the hypothesis contradicts the total miles flown in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
