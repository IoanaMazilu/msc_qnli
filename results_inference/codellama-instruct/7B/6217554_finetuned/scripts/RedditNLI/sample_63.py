jobs_premise = 255000
jobs_hypothesis = 255000
unemployment_rate_premise = 4.9
unemployment_rate_hypothesis = 4.9

# the hypothesis and premise mention the number of jobs and the unemployment rate in July
if jobs_hypothesis!= jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif unemployment_rate_hypothesis!= unemployment_rate_premise:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
