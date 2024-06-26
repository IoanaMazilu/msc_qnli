jobs_grew_premise = 161000
jobs_added_hypothesis = 161000
unemployment_rate_premise = 4.9
unemployment_rate_hypothesis = 4.9

# the hypothesis and premise mention the number of jobs added and the unemployment rate in the US economy
if jobs_grew_premise != jobs_added_hypothesis:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif unemployment_rate_hypothesis != unemployment_rate_premise:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
