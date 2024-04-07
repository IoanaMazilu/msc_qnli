# Premise: U.S. Companies Added 67,000 Jobs in August.
# Hypothesis: 67,000 Jobs Gained.
# Golden Label: neutral

jobs_added_premise = 67000
jobs_gained_hypothesis = 67000

# the hypothesis and premise mention the number of jobs added/gained
if jobs_added_premise != jobs_gained_hypothesis:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

