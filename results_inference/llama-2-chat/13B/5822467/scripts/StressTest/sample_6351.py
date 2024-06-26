profit_premise = 22000
profit_hypothesis = 42000

# the hypothesis refers to the amount of profit received by Mr. Praveen
if profit_hypothesis <= profit_premise:
    # check if the hypothesis value contradicts the estimate of the profit in the premise
    label = "contradiction"
elif profit_premise!= profit_hypothesis:
    # check if the hypothesis value contradicts the amount of profit reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
