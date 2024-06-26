grant_money_premise = 45000
grant_money_hypothesis = 45000

# the hypothesis mentions the amount of money Wheeler is accused of stealing, which is also mentioned in the premise
if grant_money_hypothesis!= grant_money_premise:
    # check if the amount of money in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the amounts are the same, we can infer entailment
    label = "entailment"

print(label)
