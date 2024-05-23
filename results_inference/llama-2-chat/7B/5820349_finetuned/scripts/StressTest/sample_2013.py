years_premise = 2
years_hypothesis = 6
interest_rate_premise = 4
interest_rate_hypothesis = 4

# the hypothesis refers to the number of years and interest rate mentioned in the premise
if years_premise >= years_hypothesis:
    # check if the number of years in the premise contradicts the estimate of less than 'years_hypothesis'
    label = "contradiction"
elif interest_rate_premise!= interest_rate_hypothesis:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)