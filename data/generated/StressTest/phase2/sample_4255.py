# Premise: Raviraj invested an amount of less than 5000000000 at compound interest rate of 10 pcpa for a period of three years.
# Hypothesis: Raviraj invested an amount of 1000000000 at compound interest rate of 10 pcpa for a period of three years.
# Golden Label: neutral

investment_premise = 5000000000
investment_hypothesis = 1000000000

# the hypothesis refers to the amount of money invested by Raviraj, mentioned also in the premise
if investment_hypothesis >= investment_premise:
    # check if the investment amount in the hypothesis contradicts the estimate of less than 'investment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment amount
    # any investment amount less than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
