jobs_premise = 450
jobs_hypothesis = 450

# The hypothesis mentions the number of jobs that the project will create, which is also referenced in the premise
if jobs_hypothesis != jobs_premise:
    # Check if the number of jobs in the hypothesis contradicts the number of jobs mentioned in the premise
    label = "contradiction"
else:
    # If the number of jobs in the hypothesis does not contradict the number of jobs in the premise, we can infer entailment
    label = "entailment"

print(label)
