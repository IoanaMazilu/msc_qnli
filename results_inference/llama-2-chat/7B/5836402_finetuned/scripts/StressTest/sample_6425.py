account_money_premise = 248
account_money_hypothesis = 148

# the hypothesis talks about the amount of money in Marie's account, referenced also in the premise
if account_money_hypothesis!= account_money_premise:
    # check if the amount of money in the hypothesis contradicts the amount of money in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
