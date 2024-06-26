stolen_money_premise = 45000
stolen_money_hypothesis = 45000

# the hypothesis mentions the amount of money stolen, which is also mentioned in the premise
if stolen_money_hypothesis!= stolen_money_premise:
    # check if the amount of money stolen in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the amount of money stolen in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
