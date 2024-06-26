friends_group_premise = 7
friends_group_hypothesis = 6

# the hypothesis refers to the number of friends in John's group, also mentioned in the premise
if friends_group_hypothesis >= friends_group_premise:
    # check if the number of friends in the hypothesis contradicts the premise of less than 'friends_group_premise'
    label = "contradiction"
else:
    # the premise provides only an upper limit for the number of friends
    # any number of friends less than 'friends_group_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
