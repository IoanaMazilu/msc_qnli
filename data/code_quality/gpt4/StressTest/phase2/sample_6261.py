job_hours_premise = 10
job_hours_hypothesis = 40

# the hypothesis refers to the time Annie can complete a job alone, mentioned also in the premise
if job_hours_hypothesis < job_hours_premise:
    # check if the hypothesis value contradicts the time reported in the premise
    label = "contradiction"
elif job_hours_hypothesis > job_hours_premise:
    # check if the hypothesis value contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
