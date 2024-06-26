num_friends_premise = 6
num_friends_hypothesis = 6

# the hypothesis refers to the number of friends mentioned in the premise
if num_friends_hypothesis < num_friends_premise:
    # check if the hypothesis value contradicts the number of friends in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of friends
    # any number of friends greater than or equal to 'num_friends_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)