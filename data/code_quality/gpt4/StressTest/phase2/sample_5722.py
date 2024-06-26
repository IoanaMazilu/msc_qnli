pencils_purchased_premise = 20
pencils_purchased_hypothesis = 70
loss_price_premise = 20
loss_price_hypothesis = 20

# the hypothesis talks about the number of pencils purchased and the loss in selling price
if pencils_purchased_hypothesis <= pencils_purchased_premise:
    # check if the hypothesis contradicts the premise of purchasing more than 'pencils_purchased_premise'
    label = "contradiction"
elif loss_price_hypothesis != loss_price_premise:
    # check if the loss in selling price in the hypothesis contradicts with the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purchased pencils
    # any number of purchased pencils greater than 'pencils_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
