money_invested_premise = 50000
money_invested_hypothesis = 10000

# the hypothesis talks about the amount of money invested in the business
if money_invested_premise <= money_invested_hypothesis:
    # check if the hypothesis value contradicts the estimate of more than'money_invested_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money invested in the business
    # any amount of money greater than'money_invested_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
