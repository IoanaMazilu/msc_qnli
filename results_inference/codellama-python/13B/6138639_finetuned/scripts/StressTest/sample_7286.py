job_salary_premise = 75000
job_salary_hypothesis = 45000
commission_premise = 15
commission_hypothesis = 55

# the hypothesis refers to the salary and commission of John's jobs mentioned in the premise
if job_salary_premise!= job_salary_hypothesis:
    # check if the salary in the hypothesis contradicts the salary in the premise
    label = "contradiction"
elif commission_hypothesis!= commission_premise:
    # check if the commission in the hypothesis contradicts the commission in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
