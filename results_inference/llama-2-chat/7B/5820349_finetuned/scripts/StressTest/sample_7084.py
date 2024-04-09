job_time_premise = 20
job_time_hypothesis = 10

# the hypothesis refers to the time Annie needs to finish a job, also mentioned in the premise
if job_time_hypothesis >= job_time_premise:
    # check if the time estimate in the hypothesis contradicts the premise
    label = "contradiction"
elif job_time_hypothesis < job_time_premise:
    # the premise gives an estimate for the time Annie needs to finish a job
    # any time less than 'job_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
