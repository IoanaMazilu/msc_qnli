sachi_investment_premise = 8000
sachi_investment_hypothesis = 2000

# the hypothesis talks about the amount invested in a fixed deposit, referenced also in the premise
if sachi_investment_hypothesis <= sachi_investment_premise:
    # check if the hypothesis value contradicts the estimate of more than'sachi_investment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount invested
    # any amount greater than'sachi_investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
