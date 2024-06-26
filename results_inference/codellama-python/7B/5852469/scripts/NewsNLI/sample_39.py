growth_premise = 0.025
growth_hypothesis = 0.025
new_jobs_premise = 2000000
new_jobs_hypothesis = 2000000

# the hypothesis mentions the growth and the job increase in the U.S., which are also mentioned in the premise
if growth_hypothesis!= growth_premise:
    # check if the growth in the hypothesis contradicts the growth reported in the premise
    label = "contradiction"
elif new_jobs_hypothesis!= new_jobs_premise:
    # check if the number of new jobs from the hypothesis contradicts the number of new jobs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
