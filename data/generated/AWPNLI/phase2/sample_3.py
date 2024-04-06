# Premise: A restaurant served 9.0 pizzas during lunch and 6.0 during dinner today.
# Hypothesis: 17.0 pizzas were served today.
# Golden Label: contradiction

pizzas_lunch_premise = 9.0
pizzas_dinner_premise = 6.0
total_pizzas_hypothesis = 17.0

# the hypothesis refers to the total number of pizzas served, which are also mentioned in the premise
# compute the total number of pizzas served in the premise
total_pizzas_premise = pizzas_lunch_premise + pizzas_dinner_premise
if total_pizzas_hypothesis != total_pizzas_premise:
    # check if the total number of pizzas in the hypothesis contradicts the total number of pizzas from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

