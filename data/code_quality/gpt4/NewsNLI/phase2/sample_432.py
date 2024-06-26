suspected_members_premise = 1000
suspected_members_hypothesis = 1000

# the hypothesis mentions the number of suspected members of a banned religious group arrested in China,
# which is also referenced in the premise
if suspected_members_hypothesis != suspected_members_premise:
    # check if the number of suspected members in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number from the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
