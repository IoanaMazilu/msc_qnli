bike_ride_duration_premise = 3
bike_ride_duration_hypothesis = 8

# the hypothesis refers to the duration of bike ride mentioned in the premise
if bike_ride_duration_premise > bike_ride_duration_hypothesis:
    # check if the duration of bike ride in the premise contradicts the duration of bike ride in the hypothesis
    label = "contradiction"
else:
    # if the duration of bike ride in the premise is less than or equal to the duration of bike ride in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
