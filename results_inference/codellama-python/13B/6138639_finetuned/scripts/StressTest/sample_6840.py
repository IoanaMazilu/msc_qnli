investment_premise = 20000
investment_hypothesis = 7

# the hypothesis talks about the amount invested by Rick, referenced also in the premise
if investment_hypothesis >= 7:
    # check if the hypothesis value contradicts the estimate of less than 'investment_hypothesis'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount invested by Rick
    # any amount invested for less than 'investment_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
