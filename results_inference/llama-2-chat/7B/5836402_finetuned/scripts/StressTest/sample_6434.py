investment_premise = 8000
investment_hypothesis = 2000
compound_interest_rate_premise = 5
compound_interest_rate_hypothesis = 5

# the hypothesis refers to the amount invested and the compound interest rate mentioned in the premise
if investment_hypothesis!= investment_premise:
    # check if the amount invested in the hypothesis contradicts the amount invested in the premise
    label = "contradiction"
elif compound_interest_rate_hypothesis!= compound_interest_rate_premise:
    # check if the compound interest rate in the hypothesis contradicts the compound interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
