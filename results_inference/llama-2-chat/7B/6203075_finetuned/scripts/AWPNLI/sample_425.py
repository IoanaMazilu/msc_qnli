toy_cost_premise = 9.05
marble_cost_premise = 4.95
football_cost_premise = 4.95
received_amount_premise = 6.52

net_amount_spent_hypothesis = 3.7

# the hypothesis refers to the net amount Mike spent on toys, which can be calculated from the premise
# compute the net amount Mike spent on toys according to the premise
net_amount_spent_premise = toy_cost_premise - (marble_cost_premise + football_cost_premise + received_amount_premise)
if net_amount_spent_hypothesis!= net_amount_spent_premise:
    # check if the net amount Mike spent on toys in the hypothesis contradicts the net amount from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(f"Net amount spent on toys: {net_amount_spent_premise}")
print(f"Net amount spent on toys in hypothesis: {net_amount_spent_hypothesis}")
