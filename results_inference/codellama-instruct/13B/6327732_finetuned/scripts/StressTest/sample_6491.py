annual_borrowing_premise = 6500
annual_borrowing_hypothesis = 1500

# the hypothesis refers to the annual borrowing amount mentioned in the premise
if annual_borrowing_hypothesis <= annual_borrowing_premise:
    # check if the estimate of 'annual_borrowing_hypothesis' contradicts the annual borrowing amount in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the annual borrowing amount
    # any annual borrowing amount greater than 'annual_borrowing_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
