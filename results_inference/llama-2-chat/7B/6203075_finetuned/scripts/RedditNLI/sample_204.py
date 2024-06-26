jobs_cut_premise = 5000
jobs_cut_hypothesis = 5000
workforce_cut_hypothesis = 5

# the hypothesis mentions the number of jobs to be cut in 2014, which is also mentioned in the premise
if jobs_cut_hypothesis!= jobs_cut_premise:
    # check if the number of jobs to be cut in the hypothesis contradicts the number of jobs to be cut in the premise
    label = "contradiction"
else:
    # if the number of jobs to be cut in the hypothesis does not contradict the number of jobs to be cut in the premise, we can infer entailment
    label = "entailment"

print(label)
