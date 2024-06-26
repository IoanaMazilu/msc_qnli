loan_period_premise = 5
loan_period_hypothesis = 6

# the hypothesis talks about the loan period, referenced also in the premise
if loan_period_hypothesis <= loan_period_premise:
    # check if the hypothesis value contradicts the estimate of more than 'loan_period_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the loan period
    # any loan period greater than 'loan_period_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
