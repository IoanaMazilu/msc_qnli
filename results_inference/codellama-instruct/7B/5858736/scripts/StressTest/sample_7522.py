friends_premise = 5
friends_hypothesis = 6
car_capacity = 5

# the hypothesis refers to the number of friends mentioned in the premise
if friends_hypothesis <= friends_premise:
    # check if the estimate of 'friends_hypothesis' contradicts the number of friends reported in the premise
    label = "contradiction"
elif car_capacity < friends_hypothesis:
    # check if the number of friends in the hypothesis contradicts the capacity of the car
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
