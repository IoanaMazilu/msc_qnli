job_time_premise = 20
job_time_hypothesis = 10

# the hypothesis refers to the time Annie needs to do a job, also mentioned in the premise
if job_time_hypothesis >= job_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'job_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time needed to do the job
    # any time less than 'job_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)