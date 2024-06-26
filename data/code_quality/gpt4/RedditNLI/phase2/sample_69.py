ratio_premise = 4/10
ratio_hypothesis = 4/10
expense_premise = 400
expense_hypothesis = 400

# the hypothesis and premise mention the same ratio of Americans unable to cover a certain expense
if ratio_premise != ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif expense_premise != expense_hypothesis:
    # check if the emergency expense in the hypothesis contradicts the emergency expense in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
