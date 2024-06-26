investment_premise = 5000
investment_hypothesis = 8000

# the hypothesis talks about the amount invested by Sachi, referenced also in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the estimate of more than 'investment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount invested
    # any amount greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
