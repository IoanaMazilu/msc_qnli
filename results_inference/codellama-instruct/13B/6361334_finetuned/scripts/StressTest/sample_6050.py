amount_premise = 95
amount_hypothesis = 55

# the hypothesis refers to the amount of money to be given to John, which is also mentioned in the premise
if amount_hypothesis <= amount_premise:
    # check if the estimate of 'amount_hypothesis' contradicts the amount of money to be given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
