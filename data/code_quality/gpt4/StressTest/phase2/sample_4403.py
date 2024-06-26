sandy_job_days_premise = 18
sandy_job_days_hypothesis = 18
molly_job_days_premise = 36
molly_job_days_hypothesis = 36

# the hypothesis refers to the time it takes for Sandy and Molly to do a job, as mentioned in the premise
if sandy_job_days_hypothesis < sandy_job_days_premise:
    # check if the time estimate in 'sandy_job_days_hypothesis' contradicts the time it takes for Sandy to do the job in the premise
    label = "contradiction"
elif molly_job_days_hypothesis != molly_job_days_premise:
    # check if the time it takes for Molly to do the job in the hypothesis contradicts the time it takes for Molly to do the job in the premise
    label = "contradiction"
else:
    # the premise gives exact times for Sandy and Molly to do the job
    # the hypothesis stating that Sandy can do the job in more than 18 days does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
