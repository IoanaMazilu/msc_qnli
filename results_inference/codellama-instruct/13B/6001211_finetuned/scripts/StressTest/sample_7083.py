job_time_premise = 10
job_time_hypothesis = 20

# the hypothesis refers to the time Annie needs to finish a job, also mentioned in the premise
if job_time_hypothesis < job_time_premise:
    # check if the hypothesis value contradicts the time reported in the premise
    label = "contradiction"
elif job_time_hypothesis == job_time_premise:
    # check if the hypothesis value is equal to the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
