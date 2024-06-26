job_hours_premise = 85
job_hours_hypothesis = 15

# the hypothesis talks about the number of hours Dan can do a job alone, which is also mentioned in the premise
if job_hours_hypothesis >= job_hours_premise:
    # check if the hypothesis value contradicts the premise statement of less than 'job_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'job_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
