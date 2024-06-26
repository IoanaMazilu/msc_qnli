annual_borrow_premise = 3500
annual_borrow_hypothesis = 6500

# the hypothesis talks about the amount Dana borrows annually, referenced also in the premise
if annual_borrow_hypothesis <= annual_borrow_premise:
    # check if the hypothesis value contradicts the estimate of more than 'annual_borrow_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the annual borrowing
    # any amount greater than 'annual_borrow_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
