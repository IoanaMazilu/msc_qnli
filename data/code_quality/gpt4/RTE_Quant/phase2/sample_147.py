nato_members_premise = 19
nato_members_hypothesis = 16

# the hypothesis talks about the number of NATO members which is also mentioned in the premise
if nato_members_hypothesis != nato_members_premise:
    # check if the number of NATO members in the hypothesis contradicts the number of NATO members from the premise
    label = "contradiction"
else:
    # if the number of NATO members in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
