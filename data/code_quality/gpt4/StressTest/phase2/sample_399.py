coffee_ounces_premise = 70
coffee_ounces_hypothesis = 30

# the hypothesis refers to the amount of coffee Carina has in ounces mentioned in the premise
if coffee_ounces_hypothesis >= coffee_ounces_premise:
    # check if the estimate of 'coffee_ounces_hypothesis' contradicts the number of coffee ounces in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
