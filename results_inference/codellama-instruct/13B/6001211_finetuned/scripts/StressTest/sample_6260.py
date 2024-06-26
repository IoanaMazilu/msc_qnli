job_time_premise = 15
job_time_hypothesis = 15

# the hypothesis refers to the time Dan takes to do a job alone, mentioned in the premise
if job_time_hypothesis <= job_time_premise:
    # check if the hypothesis value contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives an exact time for Dan to do the job
    # any time greater than 'job_time_premise' contradicts the premise
    label = "contradiction"

print(label)
