# Premise: James took a 3-hour bike ride.
# Hypothesis: James took a less than 3-hour bike ride.
# Golden Label: contradiction

bike_ride_duration_premise = 3
bike_ride_duration_hypothesis = 3

# the hypothesis refers to the bike ride duration mentioned in the premise
if bike_ride_duration_hypothesis < bike_ride_duration_premise:
    # check if the duration of 'bike_ride_duration_hypothesis' contradicts the duration of bike ride in the premise
    label = "entailment"
elif bike_ride_duration_hypothesis >= bike_ride_duration_premise:
    # check if the duration of 'bike_ride_duration_hypothesis' contradicts the duration of bike ride in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)

