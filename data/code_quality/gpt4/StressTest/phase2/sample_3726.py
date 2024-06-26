gang_members_premise = 8
gang_members_hypothesis = 2

# the hypothesis talks about the number of gang members in Andrew's gang, referenced also in the premise
if gang_members_premise <= gang_members_hypothesis:
    # check if the premise value contradicts the estimate of more than 'gang_members_hypothesis'
    label = "contradiction"
else:
    # the hypothesis gives an estimate for the number of gang members
    # the premise explicitly states the number of gang members
    # thus, if the number of gang members in the premise is greater than 'gang_members_hypothesis', we can infer entailment
    label = "entailment"

print(label)
