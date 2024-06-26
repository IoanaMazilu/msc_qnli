group_size_premise = 60
group_size_hypothesis = 20
iceland_visitors_premise = 35
iceland_visitors_hypothesis = 35
norway_visitors_premise = 23
norway_visitors_hypothesis = 23

# the hypothesis refers to the size of the group and the number of people who visited Iceland and Norway, mentioned in the premise
if group_size_premise <= group_size_hypothesis:
    # check if the estimate of 'group_size_hypothesis' contradicts the size of the group in the premise
    label = "contradiction"
elif iceland_visitors_hypothesis!= iceland_visitors_premise or norway_visitors_hypothesis!= norway_visitors_premise:
    # check if the number of visitors to Iceland or Norway in the hypothesis contradicts the number of visitors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
