job_hours_premise = 15
job_hours_hypothesis = 85

# the hypothesis refers to the number of hours Dan can do a job alone, mentioned in the premise
if job_hours_premise >= job_hours_hypothesis:
    # check if the premise contradicts the estimate of 'job_hours_hypothesis' being less than the premise
    label = "contradiction"
elif job_hours_hypothesis != job_hours_premise:
    # the premise gives only an exact number of hours
    # any number of hours less than 'job_hours_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
