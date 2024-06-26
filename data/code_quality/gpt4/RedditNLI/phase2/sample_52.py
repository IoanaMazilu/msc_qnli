jobs_added_premise = 161000
jobs_added_hypothesis = 161000
unemployment_rate_premise = 4.9
unemployment_rate_hypothesis = 4.9

# the hypothesis and premise mention the number of jobs added in the U.S. economy in October
# and the unemployment rate in the same period
if jobs_added_premise != jobs_added_hypothesis:
    # check if the number of jobs added in the hypothesis contradicts the number of jobs added in the premise
    label = "contradiction"
elif unemployment_rate_premise != unemployment_rate_hypothesis:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
