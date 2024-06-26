people_group_premise = 60
people_group_hypothesis = 20
visited_iceland_premise = 35
visited_iceland_hypothesis = 35
visited_norway_premise = 23
visited_norway_hypothesis = 23

# the hypothesis refers to the number of people in a group, the number of people who visited Iceland and the number of people who visited Norway
if people_group_premise <= people_group_hypothesis:
    # check if the estimate of 'people_group_hypothesis' contradicts the number of people in the group in the premise
    label = "contradiction"
elif visited_iceland_hypothesis!= visited_iceland_premise:
    # check if the number of people who visited Iceland in the hypothesis contradicts the number of people who visited Iceland reported in the premise
    label = "contradiction"
elif visited_norway_hypothesis!= visited_norway_premise:
    # check if the number of people who visited Norway in the hypothesis contradicts the number of people who visited Norway reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
