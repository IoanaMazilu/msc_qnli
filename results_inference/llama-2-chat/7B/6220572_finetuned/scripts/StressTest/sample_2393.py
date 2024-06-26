tshirts_bought_premise = 8
tshirts_bought_hypothesis = 8

# the hypothesis refers to the number of t-shirts bought mentioned in the premise
if tshirts_bought_hypothesis >= tshirts_bought_premise:
    # check if the estimate of 'tshirts_bought_hypothesis' contradicts the number of t-shirts bought in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
