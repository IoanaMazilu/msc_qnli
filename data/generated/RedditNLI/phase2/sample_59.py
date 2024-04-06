# Premise: Breaking: U.S. economy added 192,000 jobs last month as the unemployment rate fell to 8.9%.
# Hypothesis: Jobless rate falls to 8.9% as 192,000 private sector jobs added in February.
# Golden Label: neutral

jobs_added_premise = 192000
jobs_added_hypothesis = 192000
unemployment_rate_premise = 8.9
unemployment_rate_hypothesis = 8.9

# the hypothesis and premise mention the number of jobs added and the unemployment rate
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

