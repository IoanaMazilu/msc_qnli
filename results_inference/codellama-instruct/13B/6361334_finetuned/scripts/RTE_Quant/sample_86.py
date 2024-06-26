new_payroll_jobs_premise = 144000
unemployment_rate_premise = 5.4
unemployment_rate_hypothesis = 5.4

# the hypothesis talks about the unemployment rate, which is also mentioned in the premise
if unemployment_rate_hypothesis!= unemployment_rate_premise:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
