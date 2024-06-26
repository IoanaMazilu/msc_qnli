served_pizzas_premise = 9
returned_pizzas_premise = 6
successfully_served_pizzas_hypothesis = 3.0

# convert the hypothesis to an integer
successfully_served_pizzas_hypothesis = int(successfully_served_pizzas_hypothesis)

# compute the difference between the number of served pizzas and the number of returned pizzas
difference = served_pizzas_premise - returned_pizzas_premise

if difference!= successfully_served_pizzas_hypothesis:
    # check if the difference between the number of served and returned pizzas contradicts the hypothesis
    label = "contradiction"
elif successfully_served_pizzas_hypothesis > served_pizzas_premise:
    # check if the hypothesis entails the number of successfully served pizzas
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
