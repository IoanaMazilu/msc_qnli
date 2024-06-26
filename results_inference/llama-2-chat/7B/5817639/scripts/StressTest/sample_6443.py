grape_purchase_premise = 7
grape_purchase_hypothesis = 7
mango_purchase_premise = 9
mango_purchase_hypothesis = 9

# the hypothesis talks about the amount of grapes and mangoes purchased
if grape_purchase_hypothesis <= grape_purchase_premise:
    # check if the hypothesis value contradicts the estimate of 'grape_purchase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of grapes purchased
    # any amount of grapes greater than 'grape_purchase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

if mango_purchase_hypothesis <= mango_purchase_premise:
    # check if the hypothesis value contradicts the estimate of'mango_purchase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of mangoes purchased
    # any amount of mangoes greater than'mango_purchase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
