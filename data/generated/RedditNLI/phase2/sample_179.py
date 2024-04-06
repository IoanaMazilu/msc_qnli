# Premise: US economy adds 215,000 jobs in July.
# Hypothesis: US economy adds 215,000 jobs in July-BBC News.
# Golden Label: entailment

jobs_added_premise = 215000
jobs_added_hypothesis = 215000

# the hypothesis and premise mention the number of jobs added in the US economy
if jobs_added_hypothesis != jobs_added_premise:
    # check if the number of jobs added in the hypothesis contradicts the number of jobs added in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
