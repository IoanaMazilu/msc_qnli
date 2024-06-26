investment_premise = 20000
investment_hypothesis = 20000

# the hypothesis talks about the amount invested by Rick, referenced also in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the estimate of the amount invested in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount invested
    # any amount invested consistent with the premise is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
