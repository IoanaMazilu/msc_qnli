job_hours_premise = 10
job_hours_hypothesis = 20

# the hypothesis refers to the number of hours Annie needs to do a job, also mentioned in the premise
if job_hours_hypothesis <= job_hours_premise:
    # check if the hypothesis value contradicts the estimate of 'job_hours_premise'
    label = "contradiction"
else:
    # any number of hours greater than 'job_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
