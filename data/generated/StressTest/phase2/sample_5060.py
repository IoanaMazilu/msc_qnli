# Premise: Ravina leaves the job 3 days before the completion of the work.
# Hypothesis: Ravina leaves the job 2 days before the completion of the work.
# Golden Label: contradiction

leave_job_premise = 3
leave_job_hypothesis = 2

# the hypothesis makes a statement about the number of days before job completion that Ravina leaves, also mentioned in the premise
if leave_job_hypothesis != leave_job_premise:
    # check if the number of days in the hypothesis contradicts the number of days mentioned in the premise
    label = "contradiction"
else:
    # if the number of days in the hypothesis does not contradict the number of days mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)

