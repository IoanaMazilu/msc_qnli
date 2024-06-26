old_job_salary_premise = 75000
new_job_salary_premise = 45000
commission_premise = 0.35

old_job_salary_hypothesis = 75000
new_job_salary_hypothesis = 45000
commission_hypothesis = 0.15

# the hypothesis refers to the salaries and commissions in the premise
if old_job_salary_hypothesis!= old_job_salary_premise or new_job_salary_hypothesis!= new_job_salary_premise:
    # check if the salaries in the hypothesis contradict the salaries in the premise
    label = "contradiction"
elif commission_hypothesis >= commission_premise:
    # check if the commission in the hypothesis contradicts the commission in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the commission
    # any commission less than 'commission_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
