friends_premise = 6
friends_hypothesis = 4

# the hypothesis talks about the number of different combinations of passengers, while the premise refers to the total number of friends
if friends_hypothesis <= friends_premise:
    # check if the hypothesis value contradicts the estimate of more than 'friends_premise' combinations
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of combinations,
    # any number of combinations greater than 'friends_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
