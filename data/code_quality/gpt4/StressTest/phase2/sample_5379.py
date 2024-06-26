job_salary_premise = 75000
job_salary_hypothesis = 75000
sales_job_salary_premise = 45000
sales_job_salary_hypothesis = 45000
commission_premise = 15
commission_hypothesis = 65

# the hypothesis refers to the jobs and salary details mentioned in the premise
if job_salary_premise != job_salary_hypothesis or sales_job_salary_premise != sales_job_salary_hypothesis:
    # check if the salary details in the hypothesis contradict the salary details in the premise
    label = "contradiction"
elif commission_hypothesis <= commission_premise:
    # check if the commission percentage in the hypothesis contradicts the commission percentage in the premise
    label = "contradiction"
else:
    # the premise gives an exact figure for the commission percentage, any commission percentage less than 'commission_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
