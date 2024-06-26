job_loss_years_premise = 34
job_loss_years_hypothesis = 34

# the hypothesis and premise mention the number of years of US job loss
if job_loss_years_hypothesis!= job_loss_years_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
