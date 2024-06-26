borrowed_amount_premise = 1000
borrowed_amount_hypothesis = 6000

# the hypothesis talks about the total amount of money borrowed by Albert, referenced also in the premise
if borrowed_amount_hypothesis <= borrowed_amount_premise:
    # check if the hypothesis value contradicts the estimate of more than 'borrowed_amount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the borrowed amount
    # any borrowed amount greater than 'borrowed_amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
