wheat_purchased_premise = 30
wheat_purchased_hypothesis = 30

# the hypothesis refers to the number of kg of wheat purchased and the rate at which it was purchased
if wheat_purchased_hypothesis <= wheat_purchased_premise:
    # check if the estimate of 'wheat_purchased_hypothesis' contradicts the number of kg of wheat purchased in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of kg of wheat purchased
    # any number of kg greater than 'wheat_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
