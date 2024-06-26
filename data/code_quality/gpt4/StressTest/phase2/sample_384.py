coffee_premise = 85
coffee_hypothesis = 45

# the hypothesis refers to the amount of coffee Carina has, also mentioned in the premise
if coffee_hypothesis >= coffee_premise:
    # check if 'coffee_hypothesis' contradicts the amount of coffee in the premise
    label = "contradiction"
elif coffee_hypothesis < coffee_premise:
    # if the amount of coffee in the hypothesis is less than the amount reported in the premise, we can infer entailment
    label = "entailment"

print(label)
