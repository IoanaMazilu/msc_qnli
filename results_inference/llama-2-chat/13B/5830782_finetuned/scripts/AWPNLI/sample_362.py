served_pizzas_premise = 9
returned_pizzas_premise = 6
successful_pizzas_hypothesis = 3.0

# the hypothesis refers to the number of successful pizzas, which can be calculated from the premise
# compute the number of successful pizzas in the premise
successful_pizzas_premise = served_pizzas_premise - returned_pizzas_premise
if successful_pizzas_hypothesis!= successful_pizzas_premise:
    # check if the number of successful pizzas in the hypothesis contradicts the number of successful pizzas from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
