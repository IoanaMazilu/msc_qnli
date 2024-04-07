# Premise: Sandy can do a job in less than 58 days and Molly can do the same job in 36 days.
# Hypothesis: Sandy can do a job in 18 days and Molly can do the same job in 36 days.
# Golden Label: neutral

sandy_job_time_premise = 58
sandy_job_time_hypothesis = 18
molly_job_time_premise = 36
molly_job_time_hypothesis = 36

# the hypothesis refers to the time Sandy and Molly take to complete a job, as mentioned in the premise
if sandy_job_time_hypothesis >= sandy_job_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'sandy_job_time_premise'
    label = "contradiction"
elif molly_job_time_hypothesis != molly_job_time_premise:
    # check if the time Molly takes to complete a job in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Sandy takes
    # any time less than 'sandy_job_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

