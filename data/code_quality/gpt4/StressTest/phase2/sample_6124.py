people_group_premise = 20
people_group_hypothesis = 60
iceland_visitors_premise = 35
iceland_visitors_hypothesis = 35
norway_visitors_premise = 23
norway_visitors_hypothesis = 23

# the hypothesis talks about the number of people in a group, and the number of Iceland and Norway visitors, all mentioned in the premise
if people_group_hypothesis <= people_group_premise:
    # check if the number of people in the hypothesis contradicts the estimate of more than 'people_group_premise'
    label = "contradiction"
elif iceland_visitors_hypothesis != iceland_visitors_premise:
    # check if the number of Iceland visitors in the hypothesis contradicts the number of Iceland visitors reported in the premise
    label = "contradiction"
elif norway_visitors_hypothesis != norway_visitors_premise:
    # check if the number of Norway visitors in the hypothesis contradicts the number of Norway visitors reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people in the group
    # any number of people greater than 'people_group_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
