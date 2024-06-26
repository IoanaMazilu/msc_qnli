old_job_salary_premise = 75000
new_job_salary_premise = 45000
commission_premise = 15

old_job_salary_hypothesis = 75000
new_job_salary_hypothesis = 45000
commission_hypothesis = 55

# the hypothesis refers to the salaries and commissions of John's old and new jobs mentioned in the premise
if old_job_salary_premise!= old_job_salary_hypothesis:
    # check if the salary of the old job in the hypothesis contradicts the salary of the old job in the premise
    label = "contradiction"
elif new_job_salary_premise!= new_job_salary_hypothesis:
    # check if the salary of the new job in the hypothesis contradicts the salary of the new job in the premise
    label = "contradiction"
elif commission_premise!= commission_hypothesis:
    # check if the commission in the hypothesis contradicts the commission in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
