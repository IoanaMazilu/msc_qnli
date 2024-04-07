# Premise: Raviraj invested an amount of 100000 at compound interest rate of 10 pcpa for a period of three years.
# Hypothesis: Raviraj invested an amount of less than 600000 at compound interest rate of 10 pcpa for a period of three years.
# Golden Label: entailment

investment_premise = 100000
investment_hypothesis = 600000
interest_rate_premise = 10
interest_rate_hypothesis = 10
period_premise = 3
period_hypothesis = 3

# the hypothesis refers to the investment amount, interest rate and period mentioned in the premise
if investment_premise >= investment_hypothesis:
    # check if the 'investment_hypothesis' contradicts the investment amount in the premise
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise or period_hypothesis != period_premise:
    # check if the interest rate or period in the hypothesis contradicts the ones reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

