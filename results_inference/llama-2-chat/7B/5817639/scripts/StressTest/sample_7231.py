purchase_premise = 40
purchase_hypothesis = 30

# the hypothesis talks about the quantity of wheat purchased, which is also referred to in the premise
if purchase_hypothesis <= purchase_premise:
    # check if the hypothesis value contradicts the estimate of less than 'purchase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of wheat purchased
    # any quantity of wheat greater than 'purchase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
