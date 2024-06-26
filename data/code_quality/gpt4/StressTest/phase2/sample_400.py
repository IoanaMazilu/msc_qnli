coffee_ounces_premise = 30
coffee_ounces_hypothesis = 70

# the hypothesis refers to the amount of coffee owned by Carina mentioned in the premise
if coffee_ounces_hypothesis <= coffee_ounces_premise:
    # check if the value of 'coffee_ounces_hypothesis' contradicts the estimate of more than 'coffee_ounces_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of coffee
    # any amount of coffee greater than 'coffee_ounces_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
