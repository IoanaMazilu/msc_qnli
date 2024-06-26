job_time_premise = 2
job_time_hypothesis = 9

# the hypothesis refers to the same job time that Annie needs, mentioned in the premise
if job_time_hypothesis <= job_time_premise:
    # check if the estimated 'job_time_hypothesis' contradicts the estimate of more than 'job_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the job time
    # any job time greater than 'job_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
