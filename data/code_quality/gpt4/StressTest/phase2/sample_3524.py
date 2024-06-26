people_group_premise = 100
people_group_hypothesis = 100
iceland_visitors_premise = 55
iceland_visitors_hypothesis = 55
norway_visitors_premise = 43
norway_visitors_hypothesis = 43

# the hypothesis talks about the size of a group of people and the number of visitors to Iceland and Norway, as stated in the premise
if people_group_hypothesis > people_group_premise:
    # check if the size of the group in the hypothesis contradicts the size of the group in the premise
    label = "contradiction"
elif iceland_visitors_hypothesis != iceland_visitors_premise or norway_visitors_hypothesis != norway_visitors_premise:
    # check if the number of Iceland or Norway visitors in the hypothesis contradicts the number of visitors in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
