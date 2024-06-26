wheat_purchased_premise = 30
wheat_purchased_hypothesis = 40

# the hypothesis refers to the amount of wheat purchased mentioned in the premise
if wheat_purchased_hypothesis <= wheat_purchased_premise:
    # check if the estimate of 'wheat_purchased_hypothesis' contradicts the amount of wheat purchased in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of wheat purchased
    # any amount of wheat greater than 'wheat_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
