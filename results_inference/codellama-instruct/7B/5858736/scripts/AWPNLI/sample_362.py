pizzas_served_premise = 9
pizzas_returned_premise = 6
pizzas_successfully_served_hypothesis = 3.0

# the hypothesis refers to the number of pizzas successfully served, which is also mentioned in the premise
# compute the total number of pizzas served in the premise
total_pizzas_served_premise = pizzas_served_premise - pizzas_returned_premise
if pizzas_successfully_served_hypothesis >= total_pizzas_served_premise:
    # check if the number of successfully served pizzas from the hypothesis is greater than or equal to the number of pizzas served in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer contradiction
    label = "contradiction"

print(label)
