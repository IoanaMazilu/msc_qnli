# Premise: John has more than 5 friends who want to ride in his new car that can accommodate only 3 people at a time (John plus 2 passengers)
# Hypothesis: John has 6 friends who want to ride in his new car that can accommodate only 3 people at a time (John plus 2 passengers)
# Golden Label: neutral

friends_premise = 5
friends_hypothesis = 6
car_capacity = 3

# the hypothesis is about the number of John's friends who want to ride in his car, as mentioned in the premise
if friends_hypothesis <= friends_premise:
    # check if the number of friends in the hypothesis contradicts the estimate of more than 'friends_premise'
    label = "contradiction"
else:
    # the premise only gives an estimate of the number of friends, any number of friends greater than 'friends_premise' is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

