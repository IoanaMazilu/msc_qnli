friends_premise = 5
friends_hypothesis = 6
car_capacity = 5

# the hypothesis refers to the number of John's friends mentioned in the premise
if friends_hypothesis <= friends_premise:
    # check if the number of 'friends_hypothesis' contradicts the number of friends in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of friends
    # any number of friends greater than 'friends_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
