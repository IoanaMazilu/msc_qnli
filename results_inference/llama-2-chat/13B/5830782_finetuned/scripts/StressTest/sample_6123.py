group_size_premise = 60
group_size_hypothesis = 20
visited_iceland_premise = 35
visited_iceland_hypothesis = 35
visited_norway_premise = 23
visited_norway_hypothesis = 23

# the hypothesis refers to the size of the group, the number of people who have visited Iceland and Norway
if group_size_hypothesis >= group_size_premise:
    # check if the estimate of 'group_size_hypothesis' contradicts the size of the group in the premise
    label = "contradiction"
elif visited_iceland_hypothesis!= visited_iceland_premise:
    # check if the number of people who have visited Iceland in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif visited_norway_hypothesis!= visited_norway_premise:
    # check if the number of people who have visited Norway in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
