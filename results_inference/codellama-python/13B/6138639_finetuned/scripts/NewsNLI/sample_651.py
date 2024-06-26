offered_money_premise = 5000000
offered_money_hypothesis = 5000000

# the hypothesis mentions the amount of money offered to Trump, which is also mentioned in the premise
if offered_money_hypothesis!= offered_money_premise:
    # check if the amount of money in the hypothesis contradicts the amount of money reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
