pencils_purchased_premise = 50
pencils_purchased_hypothesis = 90
loss_premise = 40
loss_hypothesis = 40

# the hypothesis discusses the number of purchased pencils and the loss equivalent to the selling price of a certain number of pencils
if pencils_purchased_hypothesis <= pencils_purchased_premise:
    # check if the hypothesized number of purchased pencils contradicts the premise estimate of more than 'pencils_purchased_premise'
    label = "contradiction"
elif loss_hypothesis != loss_premise:
    # check if the hypothesized loss contradicts the loss reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purchased pencils
    # any number of purchased pencils greater than 'pencils_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
