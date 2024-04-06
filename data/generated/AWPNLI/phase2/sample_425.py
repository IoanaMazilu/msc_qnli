# Premise: Mike bought some toys and he bought marbles for $9.05, a football for $4.95, and received $6.52 for returning a baseball.
# Hypothesis: The net amount Mike spent on toys is 3.7.
# Golden Label: contradiction

marbles_cost_premise = 9.05
football_cost_premise = 4.95
baseball_return_premise = 6.52
net_spent_hypothesis = 3.7

# the hypothesis refers to the net spent amount, which can be computed from the premise
# compute the net spent amount in the premise
net_spent_premise = (marbles_cost_premise + football_cost_premise) - baseball_return_premise

if net_spent_hypothesis != net_spent_premise:
    # check if the net spent amount from the hypothesis contradicts the net spent amount from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

