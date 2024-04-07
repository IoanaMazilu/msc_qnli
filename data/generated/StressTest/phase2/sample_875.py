# Premise: Rathi took a loan for 6 years at the rate of 5% per annum on Simple Interest, If the total interest paid was Rs.
# Hypothesis: Rathi took a loan for 7 years at the rate of 5% per annum on Simple Interest, If the total interest paid was Rs.
# Golden Label: contradiction

loan_period_premise = 6
loan_period_hypothesis = 7
interest_rate_premise = 5
interest_rate_hypothesis = 5

# the hypothesis talks about the loan period and the interest rate, both mentioned in the premise
if loan_period_premise != loan_period_hypothesis:
    # check if the loan period in the hypothesis contradicts the loan period in the premise
    label = "contradiction"
elif interest_rate_premise != interest_rate_hypothesis:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
else:
    # the premise and hypothesis values are not contradicting, but the hypothesis cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

