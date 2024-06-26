coffee_weight_premise = 815
coffee_weight_hypothesis = 115

# the hypothesis talks about the amount of coffee Carina has, which is also referenced in the premise
if coffee_weight_hypothesis >= coffee_weight_premise:
    # check if the hypothesis weight contradicts the estimate of less than 'coffee_weight_premise'
    label = "contradiction"
elif coffee_weight_hypothesis < coffee_weight_premise:
    # the premise gives an upper limit for the coffee weight
    # any weight less than 'coffee_weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
