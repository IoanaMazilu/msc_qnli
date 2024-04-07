# Premise: Suresh can complete a job in less than 35 hours.
# Hypothesis: Suresh can complete a job in 15 hours.
# Golden Label: neutral

job_completion_time_premise = 35
job_completion_time_hypothesis = 15

# the hypothesis talks about the time Suresh needs to complete a job, which is also mentioned in the premise
if job_completion_time_hypothesis >= job_completion_time_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'job_completion_time_premise' hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the job completion time
    # any job completion time less than 'job_completion_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

