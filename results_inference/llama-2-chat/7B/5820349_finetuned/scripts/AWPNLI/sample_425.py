marbles_price_premise = 9.05
football_price_premise = 4.95
baseball_return_premise = 6.52
net_spent_hypothesis = 3.7

# the hypothesis refers to the net amount spent on toys, which can be computed from the premise
# compute the net amount spent on toys in the premise
net_spent_premise = marbles_price_premise + football_price_premise - baseball_return_premise
if net_spent_hypothesis!= net_spent_premise:
    # check if the net amount spent on toys in the hypothesis contradicts the net amount spent on toys from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
