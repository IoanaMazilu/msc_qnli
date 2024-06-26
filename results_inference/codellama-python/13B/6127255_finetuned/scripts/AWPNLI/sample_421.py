spent_premise = 145.16 - 5.84
net_spent_hypothesis = 134.7

# the hypothesis refers to the net amount that Mike spent, which can be computed from the premise
if net_spent_hypothesis!= spent_premise:
    # check if the net amount spent in the hypothesis contradicts the net amount spent from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
