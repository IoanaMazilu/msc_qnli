new_jobs_premise = 144000
new_jobs_hypothesis = 144000

# the hypothesis talks about the number of new jobs created in the last 12 months, which is also mentioned in the premise
if new_jobs_hypothesis!= new_jobs_premise:
    # check if the number of new jobs created in the hypothesis contradicts the number of new jobs created in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
