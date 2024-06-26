jobs_added_premise = 280000
jobs_added_hypothesis = 280000
unemployment_premise = 5.5
unemployment_hypothesis = 5.5

# the hypothesis and premise mention the number of jobs added in May and the unemployment rate
if jobs_added_premise != jobs_added_hypothesis:
    # check if the number of jobs added in the hypothesis contradicts the number of jobs added in the premise
    label = "contradiction"
elif unemployment_hypothesis != unemployment_premise:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
