total_pizzas_premise = 9
returned_pizzas_premise = 6
served_pizzas_hypothesis = 3.0

# the hypothesis refers to the number of pizzas served, which is also mentioned in the premise
# compute the number of pizzas successfully served in the premise
served_pizzas_premise = total_pizzas_premise - returned_pizzas_premise
if served_pizzas_hypothesis!= served_pizzas_premise:
    # check if the number of pizzas served in the hypothesis contradicts the number of pizzas served from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
