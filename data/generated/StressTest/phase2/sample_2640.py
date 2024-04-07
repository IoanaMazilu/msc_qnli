# Premise: How much loss would Indu has suffered had she given it to Bindu for 2 years at 4% per annum simple interest?
# Hypothesis: How much loss would Indu has suffered had she given it to Bindu for less than 5 years at 4% per annum simple interest?
# Golden Label: entailment

loan_period_premise = 2
loan_period_hypothesis = 5
interest_rate_premise = 4
interest_rate_hypothesis = 4

# the hypothesis refers to the loan period and interest rate mentioned in the premise
if loan_period_premise >= loan_period_hypothesis:
    # check if the estimate of 'loan_period_hypothesis' contradicts the loan period in the premise
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

