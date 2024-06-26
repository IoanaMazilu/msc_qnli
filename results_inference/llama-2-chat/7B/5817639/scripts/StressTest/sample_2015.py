loss_premise = 0
loss_hypothesis = 0

# the hypothesis talks about the number of years and interest rate, which are also mentioned in the premise
if loss_hypothesis <= loss_premise:
    # check if the hypothesis value contradicts the estimate of loss in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the loss, and the hypothesis provides an updated estimate based on different parameters
    label = "entailment"

print(label)
