shorts_price_premise = 13.99
shirt_price_premise = 12.14
jacket_return_premise = 7.43
net_money_spent_hypothesis = 17.5

# the hypothesis refers to the net money spent on clothes, which is also mentioned in the premise
# compute the net money spent on clothes in the premise
net_money_spent_premise = shorts_price_premise + shirt_price_premise - jacket_return_premise
if net_money_spent_hypothesis!= net_money_spent_premise:
    # check if the net money spent in the hypothesis contradicts the net money spent from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
