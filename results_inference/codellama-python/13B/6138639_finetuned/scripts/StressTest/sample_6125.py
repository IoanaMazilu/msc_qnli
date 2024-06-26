total_people_premise = 60
total_people_hypothesis = 40
iceland_visitors_premise = 35
iceland_visitors_hypothesis = 35
norway_visitors_premise = 23
norway_visitors_hypothesis = 23

# the hypothesis talks about the number of people in a group and the number of people who have visited Iceland and Norway, referenced also in the premise
if total_people_hypothesis!= total_people_premise:
    # check if the total number of people in the group in the hypothesis contradicts the total number of people in the premise
    label = "contradiction"
elif iceland_visitors_hypothesis!= iceland_visitors_premise:
    # check if the number of Iceland visitors in the hypothesis contradicts the number of Iceland visitors in the premise
    label = "contradiction"
elif norway_visitors_hypothesis!= norway_visitors_premise:
    # check if the number of Norway visitors in the hypothesis contradicts the number of Norway visitors in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)