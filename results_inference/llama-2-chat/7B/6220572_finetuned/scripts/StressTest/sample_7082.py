job_hours_premise = 15
job_hours_hypothesis = 75

# the hypothesis refers to the number of hours Dan can do a job alone, also mentioned in the premise
if job_hours_hypothesis <= job_hours_premise:
    # check if the estimate of 'job_hours_hypothesis' contradicts the number of hours in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours greater than 'job_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
