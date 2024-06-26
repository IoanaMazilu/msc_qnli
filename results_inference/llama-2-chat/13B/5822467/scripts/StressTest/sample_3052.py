james_bike_ride_premise = 1 # hours
james_bike_ride_hypothesis = 3 # hours

# the hypothesis refers to the duration of James' bike ride, mentioned in the premise
if james_bike_ride_premise <= james_bike_ride_hypothesis:
    # check if the estimate of 'james_bike_ride_hypothesis' contradicts the duration of James' bike ride in the premise
    label = "contradiction"
elif james_bike_ride_hypothesis > 2 * james_bike_ride_premise:
    # check if the hypothesis value contradicts the estimate of more than 'james_bike_ride_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
