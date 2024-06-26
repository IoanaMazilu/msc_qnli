old_job_salary_premise = 75000
old_job_salary_hypothesis = 75000
new_job_base_salary_premise = 45000
new_job_base_salary_hypothesis = 45000
commission_premise = 15
commission_hypothesis = 55

# the hypothesis refers to the salaries of John's old and new jobs and the commission percentage, all mentioned in the premise
if old_job_salary_premise!= old_job_salary_hypothesis:
    # check if the salary of the old job in the hypothesis contradicts the salary of the old job in the premise
    label = "contradiction"
elif new_job_base_salary_premise!= new_job_base_salary_hypothesis:
    # check if the base salary of the new job in the hypothesis contradicts the base salary of the new job in the premise
    label = "contradiction"
elif commission_premise!= commission_hypothesis:
    # check if the commission percentage in the hypothesis contradicts the commission percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
