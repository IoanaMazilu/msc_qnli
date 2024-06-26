jobs_premise = 5000
jobs_hypothesis = 5

# the premise mentions a specific number of jobs to be cut, while the hypothesis mentions a percentage of workforce reduction
if jobs_hypothesis!= jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
