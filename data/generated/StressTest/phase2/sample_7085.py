# Premise: Annie, working alone, can do the same job in just 10 hours.
# Hypothesis: Annie, working alone, can do the same job in just 30 hours.
# Golden Label: contradiction

job_time_premise = 10
job_time_hypothesis = 30

# the hypothesis statement is about the time Annie takes to complete a job, which is also mentioned in the premise
if job_time_hypothesis == job_time_premise:
    # if the time to complete the job in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"
elif job_time_hypothesis < job_time_premise:
    # if the time in the hypothesis is shorter than in the premise, it contradicts the premise
    label = "contradiction"
else:
    # if the time in the hypothesis is longer than in the premise, it also contradicts the premise
    label = "contradiction"

print(label)

