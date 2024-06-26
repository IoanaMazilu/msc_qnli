old_job_salary_premise = 75000
old_job_salary_hypothesis = 75000
new_job_base_salary_premise = 45000
new_job_base_salary_hypothesis = 45000
commission_premise = 35
commission_hypothesis = 15

# the hypothesis refers to the salaries of John's old and new jobs and the commission percentage, all mentioned in the premise
if old_job_salary_hypothesis!= old_job_salary_premise:
    # check if the salary of the old job in the hypothesis contradicts the salary of the old job in the premise
    label = "contradiction"
elif new_job_base_salary_hypothesis!= new_job_base_salary_premise:
    # check if the base salary of the new job in the hypothesis contradicts the base salary of the new job in the premise
    label = "contradiction"
elif commission_hypothesis >= commission_premise:
    # check if the commission percentage in the hypothesis contradicts the commission percentage in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the commission percentage
    # a lower commission percentage is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
