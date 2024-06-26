borrow_rate_premise = 1
borrow_rate_hypothesis = 6

# the hypothesis refers to the borrow rate mentioned in the premise
if borrow_rate_hypothesis <= borrow_rate_premise:
    # check if the hypothesis value contradicts the estimate of more than 'borrow_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the borrow rate
    # any borrow rate greater than 'borrow_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
