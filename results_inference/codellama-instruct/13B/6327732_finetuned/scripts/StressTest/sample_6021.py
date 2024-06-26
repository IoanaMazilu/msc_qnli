annual_borrowing_premise = 5000
annual_borrowing_hypothesis = 2000

# the hypothesis refers to the amount of money borrowed annually for college education, mentioned in the premise
if annual_borrowing_premise <= annual_borrowing_hypothesis:
    # check if the estimate of 'annual_borrowing_hypothesis' contradicts the amount of money borrowed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money borrowed annually
    # any amount of money greater than 'annual_borrowing_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
