# Premise: Sandy can do a job in 15 days and Molly can do the same job in 30 days.
# Hypothesis: Sandy can do a job in less than 85 days and Molly can do the same job in 30 days.
# Golden Label: entailment

sandy_job_time_premise = 15
sandy_job_time_hypothesis = 85
molly_job_time_premise = 30
molly_job_time_hypothesis = 30

# the hypothesis refers to the time Sandy and Molly need to do a job, mentioned in the premise
if sandy_job_time_hypothesis >= sandy_job_time_premise:
    # check if the estimate of 'sandy_job_time_hypothesis' contradicts the time Sandy needs in the premise
    label = "contradiction"
elif molly_job_time_hypothesis != molly_job_time_premise:
    # check if the time Molly needs in the hypothesis contradicts the time Molly needs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

