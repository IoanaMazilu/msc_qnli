investment_premise = 5000
investment_hypothesis = 8000
compound_interest_rate_premise = 5
compound_interest_rate_hypothesis = 5

# the hypothesis refers to the amount invested and the interest rate, which are also mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the estimate of more than 'investment_premise'
    label = "contradiction"
elif compound_interest_rate_hypothesis!= compound_interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount invested
    # any amount greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
