job_hours_premise = 40
job_hours_hypothesis = 10

# the hypothesis refers to the number of hours Annie needs to complete the job, also mentioned in the premise
if job_hours_hypothesis >= job_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'job_hours_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise estimate, we can infer entailment
    label = "entailment"

print(label)
