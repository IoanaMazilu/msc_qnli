job_time_premise = 10
job_time_hypothesis = 20

# the hypothesis refers to the time Annie needs to do a job, also mentioned in the premise
if job_time_premise >= job_time_hypothesis:
    # check if the estimate of 'job_time_premise' contradicts the time estimate in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
