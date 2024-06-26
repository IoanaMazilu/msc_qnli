jobs_premise = 255000
jobless_rate_premise = 4.9

# the premise mentions the number of jobs added and the unemployment rate

jobs_hypothesis = 255000

# the hypothesis also mentions the number of jobs added

if jobs_hypothesis!= jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif jobs_hypothesis == jobs_premise:
    # if the number of jobs in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the number of jobs added
    # any estimate of the number of jobs added in the hypothesis greater or equal to the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
