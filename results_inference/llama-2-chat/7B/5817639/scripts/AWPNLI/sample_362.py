served_pizzas_premise = 9
returned_pizzas_premise = 6
successfully_served_hypothesis = 3.0

# compare the number of pizzas served in the premise and hypothesis
if successfully_served_hypothesis >= served_pizzas_premise:
    # check if the number of pizzas successfully served in the hypothesis contradicts the number of pizzas served in the premise
    label = "contradiction"
elif successfully_served_hypothesis < served_pizzas_premise:
    # check if the number of pizzas successfully served in the hypothesis entails the number of pizzas served in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
