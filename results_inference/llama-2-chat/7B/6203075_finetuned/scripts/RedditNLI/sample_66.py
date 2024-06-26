unemployment_rate_premise = 7.8
unemployment_rate_hypothesis = 7.8
jobs_added_premise = 114000
jobs_added_hypothesis = 114000

# the hypothesis and premise mention the unemployment rate and the number of jobs added
if unemployment_rate_premise!= unemployment_rate_hypothesis:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
elif jobs_added_premise!= jobs_added_hypothesis:
    # check if the number of jobs added in the hypothesis contradicts the number of jobs added in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
