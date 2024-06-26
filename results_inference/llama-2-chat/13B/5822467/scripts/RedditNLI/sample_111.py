jobs_premise = 36000
rate_premise = 9.0

# the premise mentions the number of jobs added and the unemployment rate

jobs_hypothesis = 36000
rate_hypothesis = 9.0

# the hypothesis mentions the same number of jobs added and the same unemployment rate

if jobs_hypothesis!= jobs_premise or rate_hypothesis!= rate_premise:
    # check if the number of jobs or the unemployment rate in the hypothesis contradicts the premise
    label = "contradiction"
elif jobs_hypothesis == jobs_premise and rate_hypothesis == rate_premise:
    # check if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the number of jobs and the unemployment rate
    # any estimate of the number of jobs and the unemployment rate in the hypothesis consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
