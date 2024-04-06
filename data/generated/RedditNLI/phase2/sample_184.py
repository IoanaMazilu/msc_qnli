# Premise: Economy loses 11,000 jobs in November, fewest since 2007.
# Hypothesis: U.S. Economy Lost Only 11,000 Jobs in November.
# Golden Label: entailment

jobs_lost_premise = 11000
jobs_lost_hypothesis = 11000

# The hypothesis and premise mention the number of jobs lost in the economy in November
if jobs_lost_hypothesis != jobs_lost_premise:
    # Check if the number of jobs lost in the hypothesis contradicts the number of jobs lost in the premise
    label = "contradiction"
else:
    # If the number of jobs lost in the hypothesis and premise match, we can infer entailment
    label = "entailment"

print(label)

