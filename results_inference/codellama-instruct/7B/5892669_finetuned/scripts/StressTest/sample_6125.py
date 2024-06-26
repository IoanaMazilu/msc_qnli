group_size_premise = 60
group_size_hypothesis = 40
iceland_visitors_premise = 35
iceland_visitors_hypothesis = 35
norway_visitors_premise = 23
norway_visitors_hypothesis = 23

# the hypothesis refers to the size of the group, the number of people who visited Iceland and Norway, all mentioned in the premise
if group_size_premise!= group_size_hypothesis:
    # check if the size of the group in the hypothesis contradicts the size of the group in the premise
    label = "contradiction"
elif iceland_visitors_premise!= iceland_visitors_hypothesis:
    # check if the number of people who visited Iceland in the hypothesis contradicts the number of people who visited Iceland in the premise
    label = "contradiction"
elif norway_visitors_premise!= norway_visitors_hypothesis:
    # check if the number of people who visited Norway in the hypothesis contradicts the number of people who visited Norway in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
