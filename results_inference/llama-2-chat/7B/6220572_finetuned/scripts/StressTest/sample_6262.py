job_hours_premise = 40
job_hours_hypothesis = 10

# the hypothesis refers to the number of hours Annie can do the job alone, also mentioned in the premise
if job_hours_hypothesis >= job_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'job_hours_premise' hours
    label = "contradiction"
else:
    # any number of hours less than 'job_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
