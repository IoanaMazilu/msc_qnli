growth_premise = 0.021
growth_hypothesis = 0.021
new_jobs_premise = 100000
new_jobs_hypothesis = 100000

# the hypothesis mentions the economic growth and the job increase in the U.S., which are also mentioned in the premise
if growth_hypothesis!= growth_premise:
    # check if the economic growth in the hypothesis contradicts the economic growth reported in the premise
    label = "contradiction"
elif new_jobs_hypothesis!= new_jobs_premise:
    # check if the number of new jobs from the hypothesis contradicts the number of new jobs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
