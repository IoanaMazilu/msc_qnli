# Premise: James took a 3-hour bike ride.
# Hypothesis: James took a more than 2-hour bike ride.
# Golden Label: entailment

bike_ride_duration_premise = 3
bike_ride_duration_hypothesis = 2

# the hypothesis refers to James's bike ride duration mentioned in the premise
if bike_ride_duration_premise <= bike_ride_duration_hypothesis:
    # check if the estimate of 'bike_ride_duration_hypothesis' contradicts the bike ride duration in the premise
    label = "contradiction"
else:
    # if the bike ride duration in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

