# Premise: Working independently, Ann can do the same job in 9 hours.
# Hypothesis: Working independently, Ann can do the same job in 7 hours.
# Golden Label: contradiction

job_time_premise = 9
job_time_hypothesis = 7

# the hypothesis refers to the time Ann takes to do a job, also mentioned in the premise
if job_time_hypothesis != job_time_premise:
    # check if the time taken in the hypothesis contradicts the time taken in the premise
    label = "contradiction"
else:
    # if the time taken in the hypothesis does not contradict the time taken in the premise, we can infer entailment
    label = "entailment"

print(label)

