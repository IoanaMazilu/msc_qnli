old_job_salary_premise = 75000
new_job_base_salary_premise = 45000
commission_premise = 15

old_job_salary_hypothesis = 75000
new_job_base_salary_hypothesis = 45000
commission_hypothesis = 45

# the hypothesis refers to the salary of Jerry's old job, his new job's base salary and the commission percentage
if old_job_salary_premise!= old_job_salary_hypothesis:
    # check if the salary of Jerry's old job in the hypothesis contradicts the salary mentioned in the premise
    label = "contradiction"
elif new_job_base_salary_premise!= new_job_base_salary_hypothesis:
    # check if the base salary of Jerry's new job in the hypothesis contradicts the base salary mentioned in the premise
    label = "contradiction"
elif commission_hypothesis <= commission_premise:
    # check if the commission percentage in the hypothesis contradicts the commission percentage mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the commission percentage
    # any commission percentage less than 'commission_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
