friends_dinner_premise = 5
friends_dinner_hypothesis = 6

# the hypothesis talks about the number of friends going out to dinner, referenced also in the premise
if friends_dinner_hypothesis <= friends_dinner_premise:
    # check if the hypothesis value contradicts the estimate of more than 'friends_dinner_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of friends
    # any number of friends greater than 'friends_dinner_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
