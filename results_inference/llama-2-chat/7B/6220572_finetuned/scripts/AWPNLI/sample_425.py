toys_cost_premise = 9.05
marbles_cost_premise = 4.95
football_cost_premise = 6.52
net_amount_spent_hypothesis = 3.7

# the hypothesis talks about the net amount spent on toys, which is also referenced in the premise
# compute the net amount spent on toys from the premise
net_amount_spent_premise = toys_cost_premise + marbles_cost_premise + football_cost_premise
if net_amount_spent_hypothesis!= net_amount_spent_premise:
    # check if the net amount spent on toys in the hypothesis contradicts the net amount spent on toys from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
