jobs_premise = 36000
jobs_hypothesis = 36000
unemployment_rate_premise = 9.0
unemployment_rate_hypothesis = 9.0

# the hypothesis and premise mention the number of jobs added and the unemployment rate
if jobs_hypothesis!= jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif unemployment_rate_hypothesis!= unemployment_rate_premise:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the unemployment rate
    # any estimate of the unemployment rate in the hypothesis equal to 'unemployment_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
