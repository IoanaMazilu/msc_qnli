job_days_premise = 20
job_days_hypothesis = 70
james_work_days_premise = 10
james_work_days_hypothesis = 10
david_and_james_work_days_premise = 2
david_and_james_work_days_hypothesis = 2

# The hypothesis refers to the number of days James can finish the job alone and the number of days they worked together, which are mentioned in the premise
if job_days_hypothesis < job_days_premise or james_work_days_hypothesis != james_work_days_premise or david_and_james_work_days_hypothesis != david_and_james_work_days_premise:
    # Check if the number of days mentioned in the hypothesis contradicts the number of days mentioned in the premise
    label = "contradiction"
elif job_days_premise > job_days_hypothesis:
    # If the hypothesis values and estimates are less than the premise ones, we can infer entailment
    label = "entailment"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, but also do not entail the premise, then the relation is neutral
    label = "neutral"

print(label)
