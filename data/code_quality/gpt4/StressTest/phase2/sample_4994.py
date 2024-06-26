gang_members_premise = 8
gang_members_hypothesis = 1

# the hypothesis talks about the number of gang members mentioned in the premise
if gang_members_hypothesis != gang_members_premise:
    # if the number of gang members in the hypothesis contradicts the number of gang members in the premise, label as contradiction
    label = "contradiction"
else:
    # if the number of gang members in the hypothesis does not contradict the premise, the label is neutral as we cannot infer from the premise the exact number of ways Andrew can invite the gang to his house
    label = "neutral"

print(label)