jobs_created_premise = 144000
jobs_created_rate_premise = 1/5
jobs_created_rate_hypothesis = 1/5

# the hypothesis talks about the rate of new jobs created, which is also mentioned in the premise
if jobs_created_rate_hypothesis!= jobs_created_rate_premise:
    # check if the rate of new jobs created in the hypothesis contradicts the rate from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
