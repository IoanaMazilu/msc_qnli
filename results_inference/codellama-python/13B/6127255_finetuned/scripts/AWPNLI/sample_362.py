pizzas_served_premise = 9
pizzas_returned_premise = 6
pizzas_served_hypothesis = 3.0

# the hypothesis refers to the number of pizzas served, which is also mentioned in the premise
# compute the number of pizzas successfully served in the premise
pizzas_successfully_served_premise = pizzas_served_premise - pizzas_returned_premise
if pizzas_served_hypothesis!= pizzas_successfully_served_premise:
    # check if the number of pizzas served in the hypothesis contradicts the number of pizzas successfully served from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
