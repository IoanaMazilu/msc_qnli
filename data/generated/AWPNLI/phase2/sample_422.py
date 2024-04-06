# Premise: Sandy went to the mall to buy clothes and she spent 13.99 on shorts, 12.14 on a shirt, and received 7.43 for returning a jacket.
# Hypothesis: The net amount of money that Sandy spent on clothes is 18.7.
# Golden Label: entailment

shorts_premise = 13.99
shirt_premise = 12.14
returned_jacket_premise = 7.43
net_spent_hypothesis = 18.7

# the hypothesis refers to the net amount of money spent, which is also mentioned in the premise
# compute the net amount of money spent in the premise
net_spent_premise = shorts_premise + shirt_premise - returned_jacket_premise
if net_spent_hypothesis != net_spent_premise:
    # check if the net amount of money spent in the hypothesis contradicts the net amount of money spent in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

