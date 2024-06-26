total_people_premise = 60
iceland_visitors_premise = 35
norway_visitors_premise = 23

total_people_hypothesis = 20
iceland_visitors_hypothesis = 35
norway_visitors_hypothesis = 23

# the hypothesis refers to the number of people and the number of people who visited Iceland and Norway, mentioned in the premise
if total_people_hypothesis <= total_people_premise:
    # check if the estimate of 'total_people_hypothesis' contradicts the total number of people in the premise
    label = "contradiction"
elif iceland_visitors_hypothesis!= iceland_visitors_premise or norway_visitors_hypothesis!= norway_visitors_premise:
    # check if the number of Iceland and Norway visitors in the hypothesis contradicts the number of Iceland and Norway visitors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
