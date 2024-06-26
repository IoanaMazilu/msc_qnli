people_group_premise = 60
people_group_hypothesis = 20
iceland_visited_premise = 35
norway_visited_premise = 23

# the hypothesis talks about the number of people in a group and the number of people who have visited Iceland and Norway
if people_group_hypothesis <= people_group_premise:
    # check if the hypothesis value contradicts the estimate of 'people_group_premise'
    label = "contradiction"
elif iceland_visited_premise!= iceland_visited_hypothesis or norway_visited_premise!= norway_visited_hypothesis:
    # check if the number of people who have visited Iceland or Norway in the hypothesis contradicts the number of people who have visited those places in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
