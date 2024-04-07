# Premise: Suresh can complete a job in 15 hours.
# Hypothesis: Suresh can complete a job in less than 65 hours.
# Golden Label: entailment

job_completion_premise = 15
job_completion_hypothesis = 65

# the hypothesis refers to the time it takes for Suresh to complete a job, also mentioned in the premise
if job_completion_hypothesis < job_completion_premise:
    # check if the estimate of 'job_completion_hypothesis' contradicts the time given in the premise
    label = "contradiction"
elif job_completion_hypothesis == job_completion_premise:
    # if the hypothesis value equals the value from the premise, we can infer entailment
    label = "entailment"
else:
    # any time greater than 'job_completion_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

