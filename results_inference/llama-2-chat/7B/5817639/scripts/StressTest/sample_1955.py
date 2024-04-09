loss_premise = float(input("Loss premise: "))
loss_hypothesis = float(input("Loss hypothesis: "))

# the hypothesis talks about the loss incurred in a shorter time frame than the premise
if loss_hypothesis <= loss_premise:
    # check if the hypothesis value contradicts the estimate of loss incurred in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the loss incurred over a longer time frame
    # any loss value less than the premise estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
