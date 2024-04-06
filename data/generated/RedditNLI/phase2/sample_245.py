# Premise: U.S. Added 290,000 Jobs in April.
# Hypothesis: Jobs Are Up 290,000 in April.
# Golden Label: neutral

jobs_added_premise = 290000
jobs_added_hypothesis = 290000

# the hypothesis and premise mention the number of jobs added in April
if jobs_added_hypothesis != jobs_added_premise:
    # check if the number of jobs added in the hypothesis contradicts the number of jobs added in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

