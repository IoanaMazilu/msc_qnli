bike_ride_duration_premise = 3
bike_ride_duration_hypothesis = 1

# the hypothesis refers to the duration of James' bike ride mentioned in the premise
if bike_ride_duration_premise <= bike_ride_duration_hypothesis:
    # check if the estimate of 'bike_ride_duration_hypothesis' contradicts the duration of the bike ride in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)