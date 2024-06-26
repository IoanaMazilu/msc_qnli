jobs_added_premise = 280000
jobs_added_hypothesis = 280000
unemployment_rate_premise = 5.5
unemployment_rate_hypothesis = 5.5

# the hypothesis and premise refer to the number of jobs added in the U.S. in May and the unemployment rate
if jobs_added_premise != jobs_added_hypothesis:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif unemployment_rate_premise != unemployment_rate_hypothesis:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
