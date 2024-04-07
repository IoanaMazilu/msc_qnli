# Premise: Raviraj invested an amount of 10000000 at compound interest rate of 10 pcpa for a period of three years.
# Hypothesis: Raviraj invested an amount of 30000000 at compound interest rate of 10 pcpa for a period of three years.
# Golden Label: contradiction

investment_premise = 10000000
investment_hypothesis = 30000000
interest_rate_premise = 10
interest_rate_hypothesis = 10
period_premise = 3
period_hypothesis = 3

# the hypothesis refers to the same investment, interest rate and period as the premise
if investment_premise != investment_hypothesis:
    # the investment amount in the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
elif interest_rate_premise != interest_rate_hypothesis or period_premise != period_hypothesis:
    # the interest rate or period in the hypothesis contradict the ones in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we have neutrality
    # as the exact investment amount, interest rate and period are not fully entailed from the premise
    label = "neutral"

print(label)

