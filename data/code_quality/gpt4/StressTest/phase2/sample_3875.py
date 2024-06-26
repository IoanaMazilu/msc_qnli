job_completion_premise = 15
job_completion_hypothesis = 45

# The hypothesis refers to the time Suresh takes to complete a job, which is also referenced in the premise
if job_completion_hypothesis < job_completion_premise:
    # If the hypothesis value is lower than the premise value, it contradicts the premise
    label = "contradiction"
elif job_completion_hypothesis == job_completion_premise:
    # If the hypothesis value equals the premise value, it is entailed by the premise
    label = "entailment"
else:
    # If the hypothesis value is greater than the premise value, it does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
