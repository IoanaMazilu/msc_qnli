# Premise: Sandy can do a job in 12 days and Molly can do the same job in 24 days.
# Hypothesis: Sandy can do a job in 62 days and Molly can do the same job in 24 days.
# Golden Label: contradiction

sandy_job_time_premise = 12
molly_job_time_premise = 24
sandy_job_time_hypothesis = 62
molly_job_time_hypothesis = 24

# the hypothesis refers to the time Sandy and Molly need to do a job, same as in the premise
if sandy_job_time_hypothesis != sandy_job_time_premise:
    # check if the time Sandy needs to do a job in the hypothesis contradicts the time in the premise
    label = "contradiction"
elif molly_job_time_hypothesis != molly_job_time_premise:
    # check if the time Molly needs to do a job in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the times in the hypothesis do not contradict the times in the premise, we infer neutrality as the hypothesis is not exactly the same as the premise
    label = "neutral"

print(label)

