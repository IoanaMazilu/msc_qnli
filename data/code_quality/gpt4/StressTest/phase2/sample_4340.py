sandy_job_time_premise = 15
molly_job_time_premise = 30
sandy_job_time_hypothesis = 25
molly_job_time_hypothesis = 30

# the hypothesis talks about the time Sandy and Molly need to do a job, referenced also in the premise
if sandy_job_time_hypothesis != sandy_job_time_premise:
    # check if the time Sandy needs to do a job in the hypothesis contradicts the time Sandy needs to do a job in the premise
    label = "contradiction"
elif molly_job_time_hypothesis != molly_job_time_premise:
    # check if the time Molly needs to do a job in the hypothesis contradicts the time Molly needs to do a job in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
