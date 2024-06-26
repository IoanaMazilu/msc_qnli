y_true = 9
y_pred = 3.0

# the hypothesis states a number of successfully served pizzas, which can be computed from the premise
# compute the number of served pizzas in the premise
served_pizzas_premise = 9

if y_pred!= served_pizzas_premise:
    # check if the number of successfully served pizzas in the hypothesis contradicts the number of served pizzas in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
