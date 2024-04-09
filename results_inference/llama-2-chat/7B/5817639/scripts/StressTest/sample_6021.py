annual_borrowing_premise = 5000
annual_borrowing_hypothesis = 2000

# the hypothesis talks about the amount of money borrowed for college education, referenced also in the premise
if annual_borrowing_hypothesis <= annual_borrowing_premise:
    # check if the hypothesis value contradicts the estimate of 'annual_borrowing_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money borrowed
    # any amount of money borrowed greater than 'annual_borrowing_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
