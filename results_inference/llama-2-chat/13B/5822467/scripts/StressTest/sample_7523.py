friend_count_premise = 6
friend_count_hypothesis = 5

# the hypothesis refers to the number of friends who want to ride in the car
if friend_count_hypothesis <= friend_count_premise:
    # check if the hypothesis value contradicts the estimate of more than 'friend_count_premise'
    label = "contradiction"
elif friend_count_premise - friend_count_hypothesis > 1:
    # check if the number of friends left out in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
