jobs_gain_premise = 192000
jobs_gain_hypothesis = 192000
unemployment_rate_premise = 8.9
unemployment_rate_hypothesis = 8.9

# the hypothesis and the premise mention the job gains in February and the unemployment rate
if jobs_gain_premise != jobs_gain_hypothesis:
    # check if the number of jobs gained in the hypothesis contradicts the number of jobs gained in the premise
    label = "contradiction"
elif unemployment_rate_premise != unemployment_rate_hypothesis:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
