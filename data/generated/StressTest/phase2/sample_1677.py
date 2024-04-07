# Premise: Suresh can complete a job in 15 hours.
# Hypothesis: Suresh can complete a job in less than 35 hours.
# Golden Label: entailment

job_completion_time_premise = 15
job_completion_time_hypothesis = 35

# the hypothesis refers to the job completion time of Suresh mentioned in the premise
if job_completion_time_premise > job_completion_time_hypothesis:
    # check if the 'job_completion_time_premise' contradicts the time in the hypothesis
    label = "contradiction"
elif job_completion_time_premise < job_completion_time_hypothesis:
    # if the job completion time from the premise is less than the time from the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the job completion times are equal, we can also infer entailment
    label = "entailment"

print(label)

