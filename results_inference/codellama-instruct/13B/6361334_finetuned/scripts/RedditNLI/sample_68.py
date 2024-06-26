jobs_premise = 321000
jobs_hypothesis = 321000
unemployment_premise = 5.8
unemployment_hypothesis = 5.8

# the hypothesis and premise mention the number of jobs added and the unemployment rate
if jobs_premise!= jobs_hypothesis:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif unemployment_premise!= unemployment_hypothesis:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
