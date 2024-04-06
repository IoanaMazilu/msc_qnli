# Premise: Payrolls in U.S. Rose 175,000 in May, Unemployment 7.6%.
# Hypothesis: U.S. generates 175,000 jobs in May.
# Golden Label: entailment

jobs_created_premise = 175000
jobs_created_hypothesis = 175000

# the hypothesis and premise mention the number of jobs created in the U.S. in May
if jobs_created_hypothesis != jobs_created_premise:
    # check if the number of jobs created in the hypothesis contradicts the number of jobs created in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

