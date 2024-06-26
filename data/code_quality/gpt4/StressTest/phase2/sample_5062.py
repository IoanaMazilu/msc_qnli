friends_premise = 8
friends_hypothesis = 5

# the hypothesis refers to the group of friends mentioned in the premise
if friends_hypothesis >= friends_premise:
    # check if the number of friends in the hypothesis contradicts the premise statement of less than 'friends_premise'
    label = "contradiction"
else:
    # the premise gives only an upper limit for the number of friends
    # any number of friends less than 'friends_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
