# Premise: Raviraj invested an amount of 10000000 at compound interest rate of 10 pcpa for a period of three years.
# Hypothesis: Raviraj invested an amount of less than 80000000 at compound interest rate of 10 pcpa for a period of three years.
# Golden Label: entailment

investment_premise = 10000000
investment_hypothesis = 80000000
interest_rate_premise = 10
interest_rate_hypothesis = 10
investment_period_premise = 3
investment_period_hypothesis = 3

# the hypothesis refers to the investment amount, interest rate and period mentioned in the premise
if investment_premise >= investment_hypothesis:
    # check if the investment amount in the premise contradicts the estimate of 'less than investment_hypothesis'
    label = "contradiction"
elif interest_rate_premise != interest_rate_hypothesis or investment_period_premise != investment_period_hypothesis:
    # check if the interest rate or the investment period in the hypothesis contradicts those reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

