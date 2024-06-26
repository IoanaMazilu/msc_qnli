job_salary_premise = 75000
job_salary_hypothesis = 45000
commission_premise = 35
commission_hypothesis = 15

# the hypothesis refers to the salary and commission of the job mentioned in the premise
if job_salary_hypothesis!= job_salary_premise:
    # check if the salary in the hypothesis contradicts the salary reported in the premise
    label = "contradiction"
elif commission_hypothesis >= commission_premise:
    # check if the commission in the hypothesis contradicts the estimate of less than 'commission_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
