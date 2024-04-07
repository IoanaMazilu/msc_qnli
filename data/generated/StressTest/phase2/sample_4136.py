# Premise: Sandy invested a certain sum of money at 12% p.
# Hypothesis: Sandy invested a certain sum of money at less than 12% p.
# Golden Label: contradiction

investment_interest_premise = 12
investment_interest_hypothesis = 12

# The hypothesis talks about the interest rate of Sandy's investment, which is also mentioned in the premise
if investment_interest_hypothesis >= investment_interest_premise:
    # Check if the investment interest rate in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the interest rate in the hypothesis is less than the one in the premise, it does not contradict the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

