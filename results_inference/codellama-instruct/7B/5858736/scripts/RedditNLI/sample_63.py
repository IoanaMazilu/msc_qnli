jobs_premise = 255000
jobless_rate_premise = 4.9

# the hypothesis and premise mention the number of jobs added in July and the unemployment rate
if jobs_premise!= 255000:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif jobless_rate_premise!= 4.9:
    # check if the unemployment rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of jobs and unemployment rate
    # any estimate of the number of jobs and unemployment rate in the hypothesis greater or equal to 'jobs_premise' and 'jobless_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
