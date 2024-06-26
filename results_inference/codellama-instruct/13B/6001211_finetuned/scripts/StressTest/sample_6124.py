people_premise = 20
people_hypothesis = 60
iceland_visitors_premise = 35
iceland_visitors_hypothesis = 35
norway_visitors_premise = 23
norway_visitors_hypothesis = 23

# the hypothesis refers to the number of people who have visited Iceland and Norway in a group, mentioned also in the premise
if people_hypothesis <= people_premise:
    # check if the number of people in the hypothesis contradicts the estimate of more than 'people_premise'
    label = "contradiction"
elif iceland_visitors_hypothesis!= iceland_visitors_premise:
    # check if the number of Iceland visitors in the hypothesis contradicts the number of Iceland visitors reported in the premise
    label = "contradiction"
elif norway_visitors_hypothesis!= norway_visitors_premise:
    # check if the number of Norway visitors in the hypothesis contradicts the number of Norway visitors reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people greater than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
