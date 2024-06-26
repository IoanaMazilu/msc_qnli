coffee_premise = 55
coffee_hypothesis = 85

# the hypothesis refers to the amount of coffee Carina has, which is also mentioned in the premise
if coffee_premise >= coffee_hypothesis:
    # check if the actual amount of coffee Carina has contradicts the estimate of less than 'coffee_hypothesis' ounces
    label = "contradiction"
elif coffee_premise != coffee_hypothesis:
    # the premise gives an exact value for the amount of coffee Carina has
    # this value is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "neutral"
else:
    # if the amount of coffee Carina has does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
