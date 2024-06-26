friends_want_ride_premise = 5
friends_want_ride_hypothesis = 6
car_capacity_premise = 5
car_capacity_hypothesis = 5

# the hypothesis refers to the number of friends who want to ride with John and the capacity of John's car, mentioned in the premise
if friends_want_ride_hypothesis <= friends_want_ride_premise:
    # check if the number of friends in the hypothesis contradicts the estimate of more than 'friends_want_ride_premise'
    label = "contradiction"
elif car_capacity_hypothesis != car_capacity_premise:
    # check if the car capacity in the hypothesis contradicts the car capacity mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of friends
    # any number of friends greater than 'friends_want_ride_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
