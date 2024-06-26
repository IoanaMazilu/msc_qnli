gang_members_premise = 3
gang_members_hypothesis = 7

# the hypothesis talks about the number of gang members in a friendship gang, referenced also in the premise
if gang_members_hypothesis!= gang_members_premise:
    # check if the number of gang members in the hypothesis contradicts the number of gang members reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
