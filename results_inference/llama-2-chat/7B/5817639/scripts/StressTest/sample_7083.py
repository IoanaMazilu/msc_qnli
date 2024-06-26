job_time_premise = 10
job_time_hypothesis = 20

# the hypothesis talks about the time it takes Annie to do a job, referenced also in the premise
if job_time_hypothesis <= job_time_premise:
    # check if the hypothesis value contradicts the estimate of 'job_time_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the time it takes Annie to do the job
    # any time greater than 'job_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
