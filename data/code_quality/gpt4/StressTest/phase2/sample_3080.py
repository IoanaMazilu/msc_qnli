job_duration_premise = 12
job_duration_hypothesis = 12

# the hypothesis refers to the time Dan needs to do a job, which is also mentioned in the premise
if job_duration_hypothesis >= job_duration_premise:
    # check if the hypothesis value contradicts the estimate of less than 'job_duration_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact number for the job duration
    # any time less than 'job_duration_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
