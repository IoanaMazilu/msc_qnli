# Premise: Sandy can do a job in less than 52 days and Molly can do the same job in 24 days.
# Hypothesis: Sandy can do a job in 12 days and Molly can do the same job in 24 days.
# Golden Label: neutral

sandy_job_time_premise = 52
sandy_job_time_hypothesis = 12
molly_job_time_premise = 24
molly_job_time_hypothesis = 24

# the hypothesis refers to the time Sandy and Molly take to do a job, mentioned also in the premise
if sandy_job_time_hypothesis >= sandy_job_time_premise:
    # check if the estimate of 'sandy_job_time_hypothesis' contradicts that Sandy can do the job in less than 'sandy_job_time_premise' days
    label = "contradiction"
elif molly_job_time_hypothesis != molly_job_time_premise:
    # check if the time Molly is said to take to do the job in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Sandy can do a job
    # any time less than 'sandy_job_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

