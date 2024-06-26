friends_premise = 5
friends_hypothesis = 6

# the hypothesis talks about the number of friends who want to ride in John's new car, which is also referenced in the premise
if friends_hypothesis <= friends_premise:
    # check if the hypothesis value contradicts the estimate of more than 'friends_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of friends
    # any number of friends greater than 'friends_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
