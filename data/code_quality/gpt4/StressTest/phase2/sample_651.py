old_job_salary_premise = 75000
old_job_salary_hypothesis = 75000
new_job_base_salary_premise = 45000
new_job_base_salary_hypothesis = 45000
new_job_commission_premise = 15
new_job_commission_hypothesis = 75

# The hypothesis refers to the salary and commission of the old and new jobs mentioned in the premise
if old_job_salary_premise != old_job_salary_hypothesis or new_job_base_salary_premise != new_job_base_salary_hypothesis:
    # Check if the salaries in the hypothesis contradict the salaries reported in the premise
    label = "contradiction"
elif new_job_commission_hypothesis <= new_job_commission_premise:
    # Check if the commission rate in the hypothesis contradicts the commission rate reported in the premise
    label = "contradiction"
else:
    # The premise gives the exact salary and commission rate for the new job
    # Any commission rate less than 'new_job_commission_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
