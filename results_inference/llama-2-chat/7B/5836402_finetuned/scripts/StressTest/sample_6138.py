travel_time_car_premise = 7
travel_time_car_hypothesis = 4

# the hypothesis refers to the travel time from A to B and back, mentioned in the premise
if travel_time_car_hypothesis >= travel_time_car_premise:
    # check if the estimate of 'travel_time_car_hypothesis' contradicts the travel time from A to B in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
