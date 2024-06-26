borrow_rate_premise = 8
borrow_rate_hypothesis = 6

# the hypothesis talks about the borrowing rate of Nitin, referenced also in the premise
if borrow_rate_hypothesis >= borrow_rate_premise:
    # check if the hypothesis value contradicts the estimate of less than 'borrow_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the borrowing rate
    # any borrowing rate less than 'borrow_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
