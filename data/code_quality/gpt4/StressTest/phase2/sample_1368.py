job_completion_time_premise = 15
job_completion_time_hypothesis = 75

# the hypothesis talks about the time Suresh can complete a job, referenced also in the premise
if job_completion_time_hypothesis < job_completion_time_premise:
    # check if the hypothesis value contradicts the 'job_completion_time_premise'
    label = "contradiction"
elif job_completion_time_hypothesis == job_completion_time_premise:
    # the premise gives the exact time Suresh can complete a job
    # if the 'job_completion_time_hypothesis' is the same as 'job_completion_time_premise', we can infer entailment
    label = "entailment"
else:
    # any time greater than 'job_completion_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
