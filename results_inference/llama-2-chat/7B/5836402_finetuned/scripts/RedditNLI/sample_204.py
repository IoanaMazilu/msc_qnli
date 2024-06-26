jobs_premise = 5000
jobs_hypothesis = 5
percentage_jobs_hypothesis = 5 / 100

# the hypothesis and premise mention the number of jobs to be cut by Intel
if jobs_hypothesis!= jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif percentage_jobs_hypothesis > 100:
    # check if the estimated percentage of jobs in the hypothesis contradicts the premise estimate of less than 'percentage_of_jobs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of jobs
    # any estimate of the percentage in the hypothesis less than 'percentage_of_jobs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
