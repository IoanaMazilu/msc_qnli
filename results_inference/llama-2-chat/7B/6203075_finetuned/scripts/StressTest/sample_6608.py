years_premise = 2
years_hypothesis = 6
interest_rate_premise = 4
interest_rate_hypothesis = 4

# the hypothesis refers to the number of years and interest rate mentioned in the premise
if years_hypothesis!= years_premise or interest_rate_hypothesis!= interest_rate_premise:
    # check if the number of years or interest rate in the hypothesis contradicts the ones in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
