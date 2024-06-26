job_completion_time_premise = 45
job_completion_time_hypothesis = 15

# the hypothesis talks about the time Suresh takes to complete a job, referenced also in the premise
if job_completion_time_hypothesis >= job_completion_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'job_completion_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the job completion time
    # any time less than 'job_completion_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
