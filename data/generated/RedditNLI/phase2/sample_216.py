# Premise: U.S. estimated to have lost 525,000 jobs in January.
# Hypothesis: U.S. Lost Almost 600,000 Jobs In January.
# Golden Label: entailment

jobs_lost_premise = 525000
jobs_lost_hypothesis = 600000

# the hypothesis and premise mention the number of jobs lost in US in January
if jobs_lost_hypothesis > jobs_lost_premise:
    # check if the number of jobs lost in the hypothesis contradicts the number of jobs lost in the premise
    label = "contradiction"
elif jobs_lost_hypothesis < jobs_lost_premise:
    # check if the number of jobs lost in the hypothesis contradicts the number of jobs lost in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

