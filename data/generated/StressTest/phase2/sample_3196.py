# Premise: Calculate and compare the maturity values of $less than 4000 invested in each type of GIC.
# Hypothesis: Calculate and compare the maturity values of $1000 invested in each type of GIC.
# Golden Label: neutral

investment_premise = 4000
investment_hypothesis = 1000

# the hypothesis refers to the amount of investment mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the estimate of less than 'investment_premise'
    label = "contradiction"
elif investment_hypothesis < investment_premise:
    # the premise gives only an estimate for the investment
    # any investment less than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

