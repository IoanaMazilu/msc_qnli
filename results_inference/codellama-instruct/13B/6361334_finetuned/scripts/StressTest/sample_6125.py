group_size_premise = 60
group_size_hypothesis = 40
iceland_visitors_premise = 35
iceland_visitors_hypothesis = 35
norway_visitors_premise = 23
norway_visitors_hypothesis = 23

# the hypothesis refers to the number of people in a group and the number of visitors to Iceland and Norway, both mentioned in the premise
if group_size_hypothesis <= group_size_premise:
    # check if the hypothesis value contradicts the estimate of more than 'group_size_premise'
    label = "contradiction"
elif iceland_visitors_hypothesis!= iceland_visitors_premise or norway_visitors_hypothesis!= norway_visitors_premise:
    # check if the number of visitors to Iceland and Norway in the hypothesis contradicts the number of visitors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
