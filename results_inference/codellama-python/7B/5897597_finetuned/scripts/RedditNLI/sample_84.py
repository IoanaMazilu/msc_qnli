unemployment_rate_premise = 3.9
unemployment_rate_hypothesis = 3.9

# the hypothesis and premise mention the unemployment rate
if unemployment_rate_hypothesis!= unemployment_rate_premise:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the unemployment rate in the hypothesis does not contradict the unemployment rate in the premise, we can infer entailment
    label = "entailment"

print(label)