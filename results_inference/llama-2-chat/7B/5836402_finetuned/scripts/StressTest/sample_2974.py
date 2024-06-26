job_hours_premise = 85
job_hours_hypothesis = 15

# the hypothesis refers to the number of hours Dan can do a job alone, mentioned in the premise
if job_hours_hypothesis >= job_hours_premise:
    # check if the estimate of 'job_hours_hypothesis' contradicts the number of hours in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
