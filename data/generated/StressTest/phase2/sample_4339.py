# Premise: Sandy can do a job in less than 85 days and Molly can do the same job in 30 days.
# Hypothesis: Sandy can do a job in 15 days and Molly can do the same job in 30 days.
# Golden Label: neutral

sandy_job_time_premise = 85
sandy_job_time_hypothesis = 15
molly_job_time_premise = 30
molly_job_time_hypothesis = 30

# the hypothesis specifies the time Sandy and Molly can do a job, which is also mentioned in the premise
if sandy_job_time_hypothesis >= sandy_job_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'sandy_job_time_premise' days
    label = "contradiction"
elif molly_job_time_hypothesis != molly_job_time_premise:
    # check if the time Molly can do the job in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an upper limit for the time Sandy can do the job
    # any time less than 'sandy_job_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

