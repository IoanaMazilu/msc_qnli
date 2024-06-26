#job_time_premise = 15
#job_time_hypothesis = 15

# the hypothesis refers to the time Dan needs to do a job alone, also mentioned in the premise
# if the time in the hypothesis is the same as the time in the premise, it would be a contradiction
if job_time_hypothesis <= job_time_premise:
    label = "contradiction"
else:
    # the premise gives an exact number of hours Dan needs to do the job alone
    # any number of hours greater than 'job_time_premise' cannot be explicitly entailed from the premise, so it's neutral
    label = "neutral"

print(label)
