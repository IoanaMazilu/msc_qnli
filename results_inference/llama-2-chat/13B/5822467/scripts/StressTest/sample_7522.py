friend_count_premise = 5
friend_count_hypothesis = 6

# the hypothesis refers to the number of friends who want to ride in the car
if friend_count_hypothesis <= friend_count_premise:
    # check if the hypothesis value contradicts the estimate of 'friend_count_premise'
    label = "contradiction"
elif friend_count_premise!= friend_count_hypothesis:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
