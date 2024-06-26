bike_ride_duration_premise = 3
bike_ride_duration_hypothesis = 7

# the hypothesis refers to the duration of Jack's bike ride mentioned in the premise
if bike_ride_duration_premise >= bike_ride_duration_hypothesis:
    # check if the duration of bike ride in the premise contradicts the estimate of less than 'bike_ride_duration_hypothesis'
    label = "contradiction"
else:
    # if the bike ride duration in the premise is less than 'bike_ride_duration_hypothesis', we can infer entailment
    label = "entailment"

print(label)
