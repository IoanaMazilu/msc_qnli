people_group_premise = 20
people_group_hypothesis = 60
visited_iceland_premise = 35
visited_iceland_hypothesis = 35
visited_norway_premise = 23
visited_norway_hypothesis = 23

# the hypothesis refers to the number of people in a group, the number of people who have visited Iceland and the number of people who have visited Norway
if people_group_hypothesis <= people_group_premise:
    # check if the number of people in the group according to the hypothesis contradicts the estimate of more than 'people_group_premise'
    label = "contradiction"
elif visited_iceland_hypothesis!= visited_iceland_premise or visited_norway_hypothesis!= visited_norway_premise:
    # check if the number of people who have visited Iceland or Norway according to the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people in the group
    # any number of people greater than 'people_group_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
