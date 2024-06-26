percentage_paid_back_premise = 2
percentage_paid_back_hypothesis = 2

# the hypothesis talks about the percentage Dana gives back to her parents each month, which is also mentioned in the premise
if percentage_paid_back_hypothesis >= percentage_paid_back_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percentage_paid_back_premise'
    label = "contradiction"
else:
    # the premise gives a specific percentage that Dana gives back each month
    # any percentage less than 'percentage_paid_back_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
