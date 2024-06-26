bonds_purchased_premise = 4000
bonds_purchased_hypothesis = 5000

# the hypothesis refers to the value of bonds purchased by Robert mentioned in the premise
if bonds_purchased_hypothesis != bonds_purchased_premise:
    # check if the value of bonds in the hypothesis contradicts the value of bonds purchased reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
