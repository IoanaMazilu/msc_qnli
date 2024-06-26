investment_premise = 5000
investment_hypothesis = 8000
interest_rate_premise = 5
interest_rate_hypothesis = 5
years_premise = 2
years_hypothesis = 2

# the hypothesis talks about the amount invested, interest rate and years of investment, referenced also in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the estimate of more than 'investment_premise'
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise or years_hypothesis != years_premise:
    # check if the values of interest rate or years of investment in the hypothesis contradict the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount invested
    # any invested amount greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
