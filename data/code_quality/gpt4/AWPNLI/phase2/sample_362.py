served_pizzas_premise = 9
returned_pizzas_premise = 6
successfully_served_pizzas_hypothesis = 3.0

# the hypothesis refers to the number of pizzas successfully served, which can be deduced from the premise
# compute the number of successfully served pizzas in the premise
successfully_served_pizzas_premise = served_pizzas_premise - returned_pizzas_premise
if successfully_served_pizzas_hypothesis != successfully_served_pizzas_premise:
    # check if the number of successfully served pizzas in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
