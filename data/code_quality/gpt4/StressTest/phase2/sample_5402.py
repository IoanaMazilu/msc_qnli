group_size_premise = 80
group_size_hypothesis = 80
iceland_visitors_premise = 45
iceland_visitors_hypothesis = 45
norway_visitors_premise = 33
norway_visitors_hypothesis = 33

# the hypothesis refers to the group of people and the number of visitors to Iceland and Norway mentioned in the premise
if group_size_hypothesis != group_size_premise:
    # check if the size of the group in the hypothesis contradicts the size of the group reported in the premise
    label = "contradiction"
elif iceland_visitors_hypothesis != iceland_visitors_premise:
    # check if the number of Iceland visitors in the hypothesis contradicts the number of Iceland visitors reported in the premise
    label = "contradiction"
elif norway_visitors_hypothesis != norway_visitors_premise:
    # check if the number of Norway visitors in the hypothesis contradicts the number of Norway visitors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
