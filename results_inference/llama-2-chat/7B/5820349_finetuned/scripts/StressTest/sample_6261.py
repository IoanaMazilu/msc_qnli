job_hours_premise = 10
job_hours_hypothesis = 40

# the hypothesis refers to the number of hours Annie needs to finish a job, mentioned in the premise
if job_hours_premise >= job_hours_hypothesis:
    # check if the estimate of 'job_hours_premise' contradicts the number of hours in the hypothesis
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
