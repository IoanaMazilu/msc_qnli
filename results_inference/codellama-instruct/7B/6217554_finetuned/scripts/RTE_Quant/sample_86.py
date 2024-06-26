new_jobs_premise = 144000
new_jobs_per_5_premise = 1/5
new_jobs_per_5_hypothesis = 1/5

# the hypothesis talks about the number of new jobs per 5 new jobs, which is also mentioned in the premise
if new_jobs_per_5_hypothesis!= new_jobs_per_5_premise:
    # check if the number of new jobs per 5 new jobs in the hypothesis contradicts the number of new jobs per 5 new jobs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
