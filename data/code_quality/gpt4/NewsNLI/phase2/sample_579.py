raised_money_premise = 110000
raised_money_hypothesis = 110000

# the hypothesis mentions the amount of money raised, which is also mentioned in the premise
if raised_money_hypothesis != raised_money_premise:
    # check if the money raised in the hypothesis contradicts the money raised reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
