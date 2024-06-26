job_salary_premise = 75000
job_salary_hypothesis = 75000
commission_premise = 0.45
commission_hypothesis = 0.15

# the hypothesis talks about the salary and commission of Jerry's job, referenced also in the premise
if job_salary_hypothesis!= job_salary_premise:
    # check if the salary in the hypothesis contradicts the salary in the premise
    label = "contradiction"
elif commission_hypothesis > commission_premise:
    # check if the commission in the hypothesis contradicts the commission in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
