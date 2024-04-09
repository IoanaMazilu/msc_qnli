jobs_premise = 36000
unemployment_rate_premise = 9.0

# the premise gives the number of jobs added and the unemployment rate
if jobs_hypothesis == jobs_premise:
    # if the number of jobs in the hypothesis matches the number of jobs in the premise, we can infer entailment
    label = "entailment"
elif unemployment_rate_hypothesis < unemployment_rate_premise:
    # check if the estimated unemployment rate in the hypothesis contradicts the premise estimate
    label = "contradiction"
else:
    # the premise gives only an estimate for the unemployment rate
    # any estimate of the unemployment rate in the hypothesis greater or equal to the premise estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
