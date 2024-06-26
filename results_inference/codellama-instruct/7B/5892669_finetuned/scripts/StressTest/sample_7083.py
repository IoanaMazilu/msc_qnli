job_time_premise = 10
job_time_hypothesis = 20

# the hypothesis refers to the time Annie needs to finish a job, which is also mentioned in the premise
if job_time_hypothesis <= job_time_premise:
    # check if the hypothesis value contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
