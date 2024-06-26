gang_members_premise = 8
gang_members_hypothesis = 5

# the hypothesis refers to the number of Andrew's gang members mentioned in the premise
if gang_members_premise <= gang_members_hypothesis:
    # check if the estimate of 'gang_members_hypothesis' contradicts the number of gang members in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
