jobs_added_premise = 290000
jobs_added_hypothesis = 290000

# the hypothesis and premise both mention the number of jobs added in April
if jobs_added_hypothesis != jobs_added_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # if the number of jobs in the hypothesis does not contradict the number of jobs in the premise, we can infer entailment
    label = "entailment"

print(label)
