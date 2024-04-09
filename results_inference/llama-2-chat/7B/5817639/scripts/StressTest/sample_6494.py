amount_premise = 1000
amount_hypothesis = 700

# the hypothesis talks about the amount owed to parents after 4 years of college
if amount_hypothesis <= amount_premise:
    # check if the hypothesis value contradicts the estimate of 'amount_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the amount owed, and the hypothesis provides a lower limit for the amount owed
    # any amount less than 'amount_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
