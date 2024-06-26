old_job_salary_premise = 75000
old_job_salary_hypothesis = 75000
new_job_salary_premise = 45000
new_job_salary_hypothesis = 45000
commission_premise = 35
commission_hypothesis = 15

# the hypothesis refers to the salary and commission of John's old job and new job mentioned in the premise
if old_job_salary_premise != old_job_salary_hypothesis:
    # check if the salary of John's old job in the hypothesis contradicts the salary in the premise
    label = "contradiction"
elif new_job_salary_premise != new_job_salary_hypothesis:
    # check if the salary of John's new job in the hypothesis contradicts the salary in the premise
    label = "contradiction"
elif commission_hypothesis >= commission_premise:
    # check if the commission in the hypothesis contradicts the estimate of less than 'commission_premise' percent
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
