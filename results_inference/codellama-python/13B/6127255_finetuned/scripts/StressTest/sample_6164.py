wheat_purchased_premise = 30
wheat_purchased_hypothesis = 30

# the hypothesis refers to the quantity of wheat purchased, which is also mentioned in the premise
if wheat_purchased_hypothesis >= wheat_purchased_premise:
    # check if the hypothesis value contradicts the exact quantity mentioned in the premise
    label = "contradiction"
else:
    # the premise gives the exact quantity of wheat purchased
    # any quantity of wheat less than 'wheat_purchased_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
# 