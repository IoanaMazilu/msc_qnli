pizzas_served_premise = 9
pizzas_returned_premise = 6
pizzas_served_hypothesis = 3.0

# the hypothesis talks about the number of pizzas served, which is also referenced in the premise
# compute the total number of pizzas served in the premise
total_pizzas_served_premise = pizzas_served_premise - pizzas_returned_premise
if total_pizzas_served_hypothesis!= total_pizzas_served_premise:
    # check if the number of pizzas served from the hypothesis contradicts the number of pizzas served from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)