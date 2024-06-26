marbles_cost_premise = 9.05
football_cost_premise = 4.95
baseball_return_premise = 6.52
net_spent_hypothesis = 7.48

# the hypothesis refers to the net amount Mike spent, which can be computed from the premise
# compute the net amount spent in the premise
net_spent_premise = marbles_cost_premise + football_cost_premise - baseball_return_premise
if net_spent_hypothesis != net_spent_premise:
    # check if the net amount spent in the hypothesis contradicts the net amount spent from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
