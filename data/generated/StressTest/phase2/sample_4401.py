# Premise: Sandy can do a job in 18 days and Molly can do the same job in 36 days.
# Hypothesis: Sandy can do a job in less than 58 days and Molly can do the same job in 36 days.
# Golden Label: entailment

sandy_job_time_premise = 18
molly_job_time_premise = 36
sandy_job_time_hypothesis = 58
molly_job_time_hypothesis = 36

# the hypothesis refers to the time Sandy and Molly need to finish a job, which is also mentioned in the premise
if sandy_job_time_hypothesis < sandy_job_time_premise:
    # check if the hypothesis time for Sandy contradicts the time given in the premise
    label = "contradiction"
elif molly_job_time_hypothesis != molly_job_time_premise:
    # check if the time for Molly in the hypothesis contradicts the time given in the premise
    label = "contradiction"
else:
    # if the hypothesis times do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

