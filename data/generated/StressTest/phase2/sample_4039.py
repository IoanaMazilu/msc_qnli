# Premise: Raviraj invested an amount of less than 200000000 at compound interest rate of 10 pcpa for a period of three years.
# Hypothesis: Raviraj invested an amount of 100000000 at compound interest rate of 10 pcpa for a period of three years.
# Golden Label: neutral

investment_premise = 200000000
investment_hypothesis = 100000000
interest_rate_premise = 10
interest_rate_hypothesis = 10
investment_period_premise = 3
investment_period_hypothesis = 3

# the hypothesis talks about the investment, interest rate, and period mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the investment amount in the hypothesis contradicts the estimate of less than 'investment_premise'
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate mentioned in the premise
    label = "contradiction"
elif investment_period_hypothesis != investment_period_premise:
    # check if the investment period in the hypothesis contradicts the investment period mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an upper limit for the investment amount
    # any investment amount less than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

