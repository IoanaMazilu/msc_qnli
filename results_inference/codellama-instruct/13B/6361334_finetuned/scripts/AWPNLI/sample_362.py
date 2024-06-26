pizzas_served_premise = 9
pizzas_returned_premise = 6
pizzas_successfully_served_hypothesis = 3.0

# the hypothesis refers to the number of pizzas that were successfully served, which are also mentioned in the premise
# compute the total number of pizzas that were served
total_pizzas_served_premise = pizzas_served_premise - pizzas_returned_premise
if total_pizzas_served_premise!= pizzas_successfully_served_hypothesis:
    # check if the number of pizzas in the hypothesis contradicts the number of pizzas from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
