old_job_salary_premise = 75000
old_job_salary_hypothesis = 75000
new_job_salary_premise = 45000
new_job_salary_hypothesis = 45000
commission_premise = 35
commission_hypothesis = 15

# the hypothesis refers to the salaries and commission of the old and new jobs mentioned in the premise
if old_job_salary_premise!= old_job_salary_hypothesis:
    # check if the old job salary in the hypothesis contradicts the old job salary reported in the premise
    label = "contradiction"
elif new_job_salary_premise!= new_job_salary_hypothesis:
    # check if the new job salary in the hypothesis contradicts the new job salary reported in the premise
    label = "contradiction"
elif commission_hypothesis >= commission_premise:
    # check if the commission percentage in the hypothesis contradicts the commission percentage in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the commission percentage
    # any commission percentage less than 'commission_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
