bought_toys_premise = True
bought_marbles_premise = True
bought_football_premise = True
received_baseball_premise = True
spent_on_toys_premise = 9.05 + 4.95 + 6.52
net_amount_spent_on_toys_hypothesis = 3.7

# the hypothesis refers to the net amount spent on toys, which is also mentioned in the premise
# compute the net amount spent on toys from the premise
net_amount_spent_on_toys_premise = spent_on_toys_premise - received_baseball_premise
if net_amount_spent_on_toys_hypothesis!= net_amount_spent_on_toys_premise:
    # check if the net amount spent on toys in the hypothesis contradicts the net amount from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
