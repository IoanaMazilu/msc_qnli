# Premise: Sachi invested amount of 8000 in a fixed deposit for 2 years at compound interest rate of 5% per annum.
# Hypothesis: Sachi invested amount of 2000 in a fixed deposit for 2 years at compound interest rate of 5% per annum.
# Golden Label: contradiction

investment_premise = 8000
investment_hypothesis = 2000
years_premise = 2
years_hypothesis = 2
interest_rate_premise = 0.05
interest_rate_hypothesis = 0.05

# the hypothesis refers to the investment amount, duration and interest rate mentioned in the premise
if investment_hypothesis > investment_premise:
    # check if the investment amount in the hypothesis contradicts the investment amount in the premise
    label = "contradiction"
elif years_hypothesis != years_premise or interest_rate_hypothesis != interest_rate_premise:
    # check if the investment duration or interest rate in the hypothesis contradicts the duration or rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer contradiction
    label = "contradiction"

print(label)

