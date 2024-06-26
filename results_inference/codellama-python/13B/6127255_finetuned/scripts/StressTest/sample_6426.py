sale_premise = 450
sale_hypothesis = 750

# the hypothesis refers to the amount of the sale mentioned in the premise
if sale_hypothesis <= sale_premise:
    # check if the estimate of'sale_hypothesis' contradicts the sale amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
