marbles_price_premise = 9.05
football_price_premise = 4.95
returned_baseball_premise = 6.52
net_amount_hypothesis = 3.7

# the hypothesis refers to the net amount Mike spent on toys, which is also mentioned in the premise
# compute the net amount Mike spent on toys in the premise
net_amount_premise = marbles_price_premise + football_price_premise - returned_baseball_premise
if net_amount_hypothesis!= net_amount_premise:
    # check if the net amount in the hypothesis contradicts the net amount from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
