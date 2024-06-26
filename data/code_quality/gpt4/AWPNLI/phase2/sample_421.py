price_trumpet_premise = 145.16
price_songbook_premise = 5.84
net_amount_hypothesis = 134.7

# the hypothesis refers to the net amount Mike spent, which could be derived from the premise by subtracting the price of the songbook from the price of the trumpet
# compute the net amount spent in the premise
net_amount_premise = price_trumpet_premise - price_songbook_premise

if net_amount_hypothesis != net_amount_premise:
    # check if the net amount in the hypothesis contradicts the net amount from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
