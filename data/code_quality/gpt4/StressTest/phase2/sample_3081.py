job_time_premise = 9
job_time_hypothesis = 7

# the hypothesis talks about the time Annie needs to finish a job, referenced also in the premise
if job_time_hypothesis >= job_time_premise:
    # check if the hypothesis value contradicts the exact time of 'job_time_premise'
    label = "contradiction"
else:
    # the premise gives the exact time Annie needs to finish the job
    # any time less than 'job_time_premise' contradicts the premise
    label = "contradiction"

print(label)
