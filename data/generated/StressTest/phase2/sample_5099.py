# Premise: Jack took a 3-hour bike ride.
# Hypothesis: Jack took a 2-hour bike ride.
# Golden Label: contradiction

bike_ride_duration_premise = 3
bike_ride_duration_hypothesis = 2

# the hypothesis refers to the duration of Jack's bike ride mentioned in the premise
if bike_ride_duration_hypothesis == bike_ride_duration_premise:
    # check if the duration of the bike ride in the hypothesis matches the duration mentioned in the premise
    label = "entailment"
elif bike_ride_duration_hypothesis != bike_ride_duration_premise:
    # check if the duration of the bike ride in the hypothesis contradicts the duration mentioned in the premise
    label = "contradiction"

print(label)

