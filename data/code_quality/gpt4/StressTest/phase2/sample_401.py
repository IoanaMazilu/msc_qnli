coffee_ounces_premise = 70
coffee_ounces_hypothesis = 70

# The hypothesis refers to the total amount of coffee in ounces mentioned in the premise
if coffee_ounces_hypothesis >= coffee_ounces_premise:
    # check if the hypothesis contradicts the premise by suggesting Carina has less than 'coffee_ounces_premise'
    label = "contradiction"
else:
    # if the amount of coffee in the hypothesis doesn't contradict the premise, we can infer entailment
    label = "entailment"

print(label)
