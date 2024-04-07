# Premise: Raviraj invested an amount of 100000000 at compound interest rate of 10 pcpa for a period of three years.
# Hypothesis: Raviraj invested an amount of less than 200000000 at compound interest rate of 10 pcpa for a period of three years.
# Golden Label: entailment

investment_premise = 100000000
investment_hypothesis = 200000000
interest_premise = 10
interest_hypothesis = 10
period_premise = 3
period_hypothesis = 3

# the hypothesis refers to the amount invested, interest rate and period mentioned in the premise
if investment_premise >= investment_hypothesis:
    # check if the estimate of 'investment_hypothesis' contradicts the amount invested in the premise
    label = "contradiction"
elif interest_premise != interest_hypothesis or period_premise != period_hypothesis:
    # check if the interest rate or period in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

