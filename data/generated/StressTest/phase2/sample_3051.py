# Premise: James took a 3-hour bike ride.
# Hypothesis: James took a more than 1-hour bike ride.
# Golden Label: entailment

bike_ride_duration_premise = 3
bike_ride_duration_hypothesis = 1

# the hypothesis refers to the bike ride duration James took, which is also mentioned in the premise
if bike_ride_duration_premise <= bike_ride_duration_hypothesis:
    # check if the stipulation of 'bike_ride_duration_hypothesis' contradicts the bike ride duration in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

