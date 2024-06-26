jobless_rate_premise = 7.8
jobs_added_premise = 114000
jobless_rate_hypothesis = 7.8
jobs_added_hypothesis = 114000

# the hypothesis and premise mention the unemployment rate and the number of jobs added
if jobless_rate_hypothesis!= jobless_rate_premise:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
elif jobs_added_hypothesis!= jobs_added_premise:
    # check if the number of jobs added in the hypothesis contradicts the number of jobs added in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
