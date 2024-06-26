toys_price_premise = 9.05
marbles_price_premise = 4.95
football_price_premise = 4.95
received_amount_premise = 6.52
total_amount_spent_premise = toys_price_premise + marbles_price_premise + football_price_premise
net_amount_spent_hypothesis = 3.7

# the hypothesis refers to the net amount spent, which is also computed in the premise
# compute the net amount spent from the premise
net_amount_spent_premise = total_amount_spent_premise - received_amount_premise
if net_amount_spent_hypothesis!= net_amount_spent_premise:
    # check if the net amount spent from the hypothesis contradicts the net amount spent from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
