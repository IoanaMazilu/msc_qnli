job_completion_premise = 65
job_completion_hypothesis = 15

# the hypothesis talks about the time Suresh can complete a job, referenced also in the premise
if job_completion_hypothesis >= job_completion_premise:
    # check if the hypothesis value contradicts the estimate of less than 'job_completion_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time of job completion
    # any time less than 'job_completion_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
