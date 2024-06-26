dana_borrowing_premise = 5000
dana_borrowing_hypothesis = 3000

# the hypothesis refers to the same amount as the premise
if dana_borrowing_hypothesis <= dana_borrowing_premise:
    # check if the estimate of 'dana_borrowing_hypothesis' contradicts the number of 'dana_borrowing_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money Dana borrows annually for her college education
    # any amount greater than 'dana_borrowing_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
