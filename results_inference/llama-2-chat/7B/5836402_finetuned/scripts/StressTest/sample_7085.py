job_hours_premise = 10
job_hours_hypothesis = 30

# the hypothesis refers to the job hours mentioned in the premise
if job_hours_hypothesis <= job_hours_premise:
    # check if the hypothesis value contradicts the estimate of 'job_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the job hours
    # any job hours greater than 'job_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
