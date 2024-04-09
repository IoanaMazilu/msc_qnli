discount_premise = 10
discount_hypothesis = 30

# the hypothesis talks about a higher discount than the premise
if discount_hypothesis >= discount_premise:
    # check if the hypothesis value contradicts the estimate of more than 'discount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any discount greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
