premise_earnings = 9000
hypothesis_earnings = 8000

# the hypothesis talks about the number of earnings, referenced also in the premise
if hypothesis_earnings >= premise_earnings:
    # check if the hypothesis value contradicts the estimate of less than 'premise_earnings'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of earnings
    # any number of earnings less than 'premise_earnings' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
