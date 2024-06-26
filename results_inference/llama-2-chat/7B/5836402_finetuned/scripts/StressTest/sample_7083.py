job_hours_premise = 10
job_hours_hypothesis = 20

# the hypothesis refers to the number of hours Annie can work alone to complete a job, mentioned in the premise
if job_hours_hypothesis <= job_hours_premise:
    # check if the hypothesis value contradicts the estimate of 'job_hours_premise'
    label = "contradiction"
elif job_hours_hypothesis > job_hours_premise:
    # check if the hypothesis value is greater than the premise estimate, but less than twice the premise estimate
    label = "entailment"
else:
    # if the hypothesis value is greater than twice the premise estimate, it contradicts the premise
    label = "contradiction"

print(label)
