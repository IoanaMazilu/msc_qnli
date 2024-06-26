shorts_premise = 13.99
shirt_premise = 12.14
received_premise = 7.43
net_spent_hypothesis = 17.5

# the hypothesis refers to the net amount of money spent on clothes, which can be computed from the premise
# compute the net amount of money spent on clothes in the premise
net_spent_premise = shorts_premise + shirt_premise - received_premise
if net_spent_hypothesis!= net_spent_premise:
    # check if the net amount of money spent in the hypothesis contradicts the net amount of money spent from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
