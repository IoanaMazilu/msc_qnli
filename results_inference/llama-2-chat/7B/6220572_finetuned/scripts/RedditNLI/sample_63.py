jobs_premise = 255000
jobs_hypothesis = 255000
unemployment_rate_premise = 4.9
unemployment_rate_hypothesis = 4.9

# the hypothesis and premise mention the number of jobs added and the unemployment rate
if jobs_hypothesis!= jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif unemployment_rate_hypothesis!= unemployment_rate_premise:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of jobs and the unemployment rate
    # any estimate of the number of jobs or unemployment rate in the hypothesis consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
