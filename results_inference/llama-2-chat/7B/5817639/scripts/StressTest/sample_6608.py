loss_premise = 0
loss_hypothesis = 0

# the hypothesis talks about the number of years and interest rate, referenced also in the premise
if loss_hypothesis <= loss_premise:
    # check if the hypothesis value contradicts the estimate of 'loss_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years and interest rate
    # any number of years and interest rate combination greater than 'loss_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
