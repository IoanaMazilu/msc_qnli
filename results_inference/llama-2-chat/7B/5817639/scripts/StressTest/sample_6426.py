amount_premise = 450
amount_hypothesis = 750

# the hypothesis talks about the amount sold to George, referenced also in the premise
if amount_hypothesis <= amount_premise:
    # check if the hypothesis value contradicts the estimate of 'amount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount sold
    # any amount greater than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
