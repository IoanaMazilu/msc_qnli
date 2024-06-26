annual_borrow_premise = 2000
annual_borrow_hypothesis = 5000

# the hypothesis provides a specific amount that Dana borrows annually for her college education
# this is compared to the premise which provides an estimate of the amount
if annual_borrow_hypothesis <= annual_borrow_premise:
    # check if the hypothesis value contradicts the premise which states the borrowed amount is more than 2000 pounds
    label = "contradiction"
else:
    # the premise only provides an estimate for the amount borrowed
    # any amount greater than 'annual_borrow_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
