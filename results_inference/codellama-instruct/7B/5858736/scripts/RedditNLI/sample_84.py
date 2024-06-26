unemployment_rate_premise = 3.9
unemployment_rate_hypothesis = 3.9
wage_growth_premise = 0
wage_growth_hypothesis = 0

# the hypothesis and premise mention the unemployment rate and wage growth
if unemployment_rate_premise!= unemployment_rate_hypothesis:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
elif wage_growth_premise!= wage_growth_hypothesis:
    # check if the wage growth in the hypothesis contradicts the wage growth in the premise
    label = "contradiction"
else:
    # if the unemployment rate and wage growth in the hypothesis are consistent with the premise, we can infer entailment
    label = "entailment"

print(label)
