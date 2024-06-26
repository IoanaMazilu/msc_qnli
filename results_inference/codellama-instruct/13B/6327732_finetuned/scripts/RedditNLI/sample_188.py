jobs_premise = 255000
jobs_hypothesis = 179000

# the hypothesis and premise mention the number of jobs added in the private sector
if jobs_hypothesis < jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # if the number of jobs in the hypothesis is greater or equal to the number of jobs in the premise, we can infer entailment
    label = "entailment"

print(label)
