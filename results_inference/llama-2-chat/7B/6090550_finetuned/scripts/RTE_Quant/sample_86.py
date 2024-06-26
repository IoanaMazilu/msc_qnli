jobs_created_premise = 144000
jobs_created_hypothesis = 1/5

# the hypothesis refers to the number of jobs created, which is also mentioned in the premise
# compute the fraction of jobs created in the premise
jobs_created_premise_fraction = jobs_created_premise / 100
if jobs_created_hypothesis!= jobs_created_premise_fraction:
    # check if the fraction of jobs created in the hypothesis contradicts the fraction of jobs created in the premise
    label = "contradiction"
else:
    # if the fractions match, we can infer entailment
    label = "entailment"

print(label)
