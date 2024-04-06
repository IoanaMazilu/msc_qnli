# Premise: U.S. private sector adds 253,000 jobs in May: ADP.
# Hypothesis: U.S. Private Sector Adds 253,000 Jobs In May, More Than Expected.
# Golden Label: neutral

jobs_added_premise = 253000
jobs_added_hypothesis = 253000

# the hypothesis and premise mention the number of jobs added in the U.S. private sector in May
if jobs_added_hypothesis != jobs_added_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # if the number of jobs in the hypothesis does not contradict the number of jobs in the premise, we can infer entailment
    label = "entailment"

print(label)

