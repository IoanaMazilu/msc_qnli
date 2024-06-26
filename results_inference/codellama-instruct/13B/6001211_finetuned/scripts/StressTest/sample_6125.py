group_size_premise = 60
group_size_hypothesis = 40
iceland_visitors_premise = 35
iceland_visitors_hypothesis = 35
norway_visitors_premise = 23
norway_visitors_hypothesis = 23

# the hypothesis refers to the same group of people, their visits to Iceland and Norway, and their total size, mentioned in the premise
if group_size_hypothesis!= group_size_premise:
    # check if the group size in the hypothesis contradicts the group size reported in the premise
    label = "contradiction"
elif iceland_visitors_hypothesis!= iceland_visitors_premise:
    # check if the number of Iceland visitors in the hypothesis contradicts the number of Iceland visitors reported in the premise
    label = "contradiction"
elif norway_visitors_hypothesis!= norway_visitors_premise:
    # check if the number of Norway visitors in the hypothesis contradicts the number of Norway visitors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
