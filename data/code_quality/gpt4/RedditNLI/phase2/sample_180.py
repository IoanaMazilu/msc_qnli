mortgage_years_premise = 30
mortgage_rate_premise = 4
mortgage_years_hypothesis = 30
mortgage_rate_hypothesis = 4

# the hypothesis and premise mention the duration of a mortgage and its rate
if mortgage_years_premise != mortgage_years_hypothesis:
    # check if the mortgage duration in the hypothesis contradicts the mortgage duration in the premise
    label = "contradiction"
elif mortgage_rate_hypothesis != mortgage_rate_premise:
    # check if the mortgage rate in the hypothesis contradicts the mortgage rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
