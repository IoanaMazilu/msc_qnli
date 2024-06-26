wheat_purchased_premise = 30
wheat_purchased_hypothesis = 30

# the hypothesis talks about the quantity of wheat purchased, mentioned also in the premise
if wheat_purchased_hypothesis >= wheat_purchased_premise:
    # check if the hypothesis value contradicts the exact quantity of 'wheat_purchased_premise'
    label = "contradiction"
else:
    # the premise gives the exact quantity of wheat purchased
    # any quantity of wheat equal to 'wheat_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
