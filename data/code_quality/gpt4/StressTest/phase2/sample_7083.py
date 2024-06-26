job_hours_premise = 10
job_hours_hypothesis = 20

# the hypothesis refers to the number of hours Annie can complete the job alone, mentioned in the premise
if job_hours_premise >= job_hours_hypothesis:
    # check if the 'job_hours_premise' contradicts the estimate of less than 'job_hours_hypothesis' in the hypothesis
    label = "contradiction"
else:
    # if the 'job_hours_premise' is less than 'job_hours_hypothesis', it is consistent with the hypothesis, hence we can infer entailment
    label = "entailment"

print(label)
