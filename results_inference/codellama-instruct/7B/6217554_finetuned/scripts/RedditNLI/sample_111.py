jobs_added_premise = 36000
jobs_added_hypothesis = 36000
unemployment_rate_premise = 9.0
unemployment_rate_hypothesis = 9.0

# the hypothesis and premise mention the number of jobs added and the unemployment rate
if jobs_added_hypothesis!= jobs_added_premise:
    # check if the number of jobs added in the hypothesis contradicts the number of jobs added in the premise
    label = "contradiction"
elif unemployment_rate_hypothesis!= unemployment_rate_premise:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
