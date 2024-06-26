loss_premise = 0
loss_hypothesis = 0

# the hypothesis talks about the loss incurred by Indu had she given it to Bindu for less than 6 years at 4% per annum simple interest
if loss_hypothesis <= loss_premise:
    # check if the hypothesis value contradicts the estimate of the loss incurred by Indu in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the loss, and any loss value less than 'loss_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
