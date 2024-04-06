# Premise: Apple commits to contribute over $350 billion into US economy over the next five years, create 20,000 jobs.
# Hypothesis: Apple Says It Will Repatriate $250 Billion to US in Next Five Years, Add 20,000 Jobs in the US.
# Golden Label: entailment

contribution_premise = 350
contribution_hypothesis = 250
jobs_premise = 20000
jobs_hypothesis = 20000

# the hypothesis and premise mention the amount Apple commits to contribute to the US economy and the number of jobs it will create
if contribution_hypothesis > contribution_premise:
    # check if the contribution amount in the hypothesis contradicts the contribution amount in the premise
    label = "contradiction"
elif jobs_premise != jobs_hypothesis:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, but the contribution amount in the hypothesis is less than in the premise
    label = "neutral"

print(label)

