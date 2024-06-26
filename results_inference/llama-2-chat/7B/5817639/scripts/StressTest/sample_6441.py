purchase_premise = 7
purchase_hypothesis = 1

# the hypothesis talks about the total amount of grapes and mangoes purchased
if purchase_hypothesis <= purchase_premise:
    # check if the hypothesis value contradicts the estimate of 'purchase_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the total amount of grapes and mangoes purchased
    # any total amount of grapes and mangoes greater than 'purchase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
