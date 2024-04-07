# Premise: Sandy can do a job in less than 41 days and Molly can do the same job in 42 days.
# Hypothesis: Sandy can do a job in 21 days and Molly can do the same job in 42 days.
# Golden Label: neutral

sandy_job_time_premise = 41
molly_job_time_premise = 42
sandy_job_time_hypothesis = 21
molly_job_time_hypothesis = 42

# the hypothesis refers to the time Sandy and Molly can do a job, as mentioned in the premise
if sandy_job_time_hypothesis >= sandy_job_time_premise:
    # check if the time 'sandy_job_time_hypothesis' contradicts the time Sandy can do a job as stated in premise
    label = "contradiction"
elif molly_job_time_hypothesis != molly_job_time_premise:
    # check if the time Molly can do a job in hypothesis contradicts the time Molly can do a job as reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

