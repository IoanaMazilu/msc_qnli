friends_group_premise = 6
friends_group_hypothesis = 6

# the hypothesis refers to the number of people in John's group of friends
if friends_group_hypothesis >= friends_group_premise:
    # check if the hypothesis stating 'more than friends_group_hypothesis' contradicts the exact number in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
