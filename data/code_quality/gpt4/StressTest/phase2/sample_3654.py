group_people_premise = 90
group_people_hypothesis = 60
iceland_visitors_premise = 55
iceland_visitors_hypothesis = 55
norway_visitors_premise = 33
norway_visitors_hypothesis = 33

# the hypothesis refers to the number of people in a group, as well as the number of people who have visited Iceland and Norway, which are also mentioned in the premise
if group_people_premise <= group_people_hypothesis:
    # check if the group size in the premise contradicts the estimate of more than 'group_people_hypothesis'
    label = "contradiction"
elif iceland_visitors_hypothesis != iceland_visitors_premise:
    # check if the number of Iceland visitors in the hypothesis contradicts the number of Iceland visitors reported in the premise
    label = "contradiction"
elif norway_visitors_hypothesis != norway_visitors_premise:
    # check if the number of Norway visitors in the hypothesis contradicts the number of Norway visitors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
