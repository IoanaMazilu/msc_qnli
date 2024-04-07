# Premise: James took a 3-hour bike ride.
# Hypothesis: James took a 8-hour bike ride.
# Golden Label: contradiction

bike_ride_time_premise = 3
bike_ride_time_hypothesis = 8

# the hypothesis refers to the duration of James' bike ride mentioned in the premise
if bike_ride_time_hypothesis == bike_ride_time_premise:
    # check if the duration of the bike ride in the hypothesis matches the duration in the premise
    label = "entailment"
else:
    # if the duration of the bike ride in the hypothesis does not match the duration in the premise, we can infer contradiction
    label = "contradiction"

print(label)

