jobs_added_premise = 321000
jobs_added_hypothesis = 321000
unemployment_rate_premise = 5.8
unemployment_rate_hypothesis = 5.8

# the hypothesis and premise mention the number of jobs added in the U.S. in November and the unemployment rate
if jobs_added_premise!= jobs_added_hypothesis:
    # check if the number of jobs added in the hypothesis contradicts the number of jobs added in the premise
    label = "contradiction"
elif unemployment_rate_premise!= unemployment_rate_hypothesis:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)