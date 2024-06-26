group_size_premise = 20
group_size_hypothesis = 60
iceland_visitors_premise = 35
iceland_visitors_hypothesis = 35
norway_visitors_premise = 23
norway_visitors_hypothesis = 23

# the hypothesis refers to the size of the group and the number of visitors to Iceland and Norway mentioned in the premise
if group_size_hypothesis <= group_size_premise:
    # check if the group size in the hypothesis contradicts the estimate of more than 'group_size_premise'
    label = "contradiction"
elif iceland_visitors_hypothesis!= iceland_visitors_premise or norway_visitors_hypothesis!= norway_visitors_premise:
    # check if the number of visitors to Iceland or Norway in the hypothesis contradicts the number of visitors reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the group size
    # any group size greater than 'group_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
