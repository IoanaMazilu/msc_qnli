job_time_premise = 25
job_time_hypothesis = 15

# the hypothesis talks about the time Dan needs to do a job, referenced also in the premise
if job_time_hypothesis >= job_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'job_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time less than 'job_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)