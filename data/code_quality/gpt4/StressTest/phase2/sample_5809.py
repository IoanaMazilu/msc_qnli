old_job_salary = 75000
new_job_base_salary = 45000
new_job_commission_premise = 55
new_job_commission_hypothesis = 15

# the hypothesis talks about the salaries and commissions of Sid's jobs, referenced also in the premise
if old_job_salary != new_job_base_salary:
    # check if the base salary in the hypothesis contradicts the base salary in the premise
    label = "contradiction"
elif new_job_commission_hypothesis >= new_job_commission_premise:
    # check if the commission in the hypothesis contradicts the estimate of less than 'new_job_commission_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the commission
    # any commission less than 'new_job_commission_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
