job_completion_time_premise = 15
job_completion_time_hypothesis = 85

# the hypothesis talks about the time Suresh takes to complete a job, which is also mentioned in the premise
if job_completion_time_premise > job_completion_time_hypothesis:
    # check if the premise value contradicts the hypothesis estimate of less than 'job_completion_time_hypothesis'
    label = "contradiction"
else:
    # the hypothesis value does not contradict the premise, and can be explicitly entailed from the premise
    label = "entailment"

print(label)
