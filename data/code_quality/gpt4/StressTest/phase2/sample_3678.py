job_completion_time_premise = 15
job_completion_time_hypothesis = 25

# the hypothesis refers to the time taken by Suresh to complete a job, also mentioned in the premise
if job_completion_time_premise >= job_completion_time_hypothesis:
    # check if the time taken for job completion in premise contradicts the estimate of less than 'job_completion_time_hypothesis'
    label = "contradiction"
else:
    # if the time taken for job completion in premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
