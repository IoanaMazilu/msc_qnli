wheat_purchased_premise = 40
wheat_purchased_hypothesis = 30

# the hypothesis talks about the quantity of wheat purchased by Arun, referenced also in the premise
if wheat_purchased_hypothesis >= wheat_purchased_premise:
    # check if the hypothesis value contradicts the estimate of less than 'wheat_purchased_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of wheat
    # any quantity of wheat less than 'wheat_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
