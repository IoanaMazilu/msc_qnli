gang_members_premise = 8
gang_members_hypothesis = 3

# the hypothesis refers to the number of gang members Andrew has, which is also mentioned in the premise
if gang_members_premise <= gang_members_hypothesis:
    # check if the estimate of 'gang_members_hypothesis' contradicts the number of gang members in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
