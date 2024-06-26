unemployment_rate_premise = 3.9
job_growth_hypothesis = 3.9

# check if the unemployment rate in the hypothesis contradicts the premise
if unemployment_rate_premise!= job_growth_hypothesis:
    label = "contradiction"
else:
    # if the unemployment rate in the hypothesis is the same as in the premise, and the job growth in the hypothesis is greater than or equal to the premise, we can infer entailment
    label = "entailment"

print(label)
