current_account_drains_premise = 5.12
current_account_drains_hypothesis = 1

# the hypothesis and premise mention the amount of money drained from the economy by the current account
if current_account_drains_hypothesis!= current_account_drains_premise:
    # check if the amount of money in the hypothesis contradicts the amount of money in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
