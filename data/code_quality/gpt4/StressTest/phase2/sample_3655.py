group_size_premise = 60
group_size_hypothesis = 90
iceland_visitors_premise = 55
iceland_visitors_hypothesis = 55
norway_visitors_premise = 33
norway_visitors_hypothesis = 33

# the hypothesis refers to the group size and the number of visitors to Iceland and Norway mentioned in the premise
if group_size_hypothesis <= group_size_premise:
    # check if the 'group_size_hypothesis' contradicts the estimate of more than 'group_size_premise' people
    label = "contradiction"
elif iceland_visitors_hypothesis != iceland_visitors_premise or norway_visitors_hypothesis != norway_visitors_premise:
    # check if the number of visitors to Iceland or Norway in the hypothesis contradicts the number of visitors reported in the premise
    label = "contradiction"
else:
    # the premise only provides an estimate for the group size
    # any group size greater than 'group_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
