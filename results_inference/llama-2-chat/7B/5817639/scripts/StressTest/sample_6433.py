invested_amount_premise = 5000
invested_amount_hypothesis = 8000
compound_interest_rate_premise = 5
compound_interest_rate_hypothesis = 5

# the hypothesis talks about the amount of money invested and the compound interest rate, both mentioned in the premise
if invested_amount_hypothesis <= invested_amount_premise:
    # check if the hypothesis value contradicts the estimate of more than 'invested_amount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money invested
    # any amount of money greater than 'invested_amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
