job_hours_premise = 10
job_hours_hypothesis = 40

# the hypothesis refers to the job hours, which is also mentioned in the premise
if job_hours_hypothesis <= job_hours_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it does not contradict the premise
    # but it also does not entail the premise, since the premise gives a specific value for the job hours
    label = "neutral"

print(label)
