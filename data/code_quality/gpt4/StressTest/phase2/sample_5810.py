old_job_salary_premise = 75000
old_job_salary_hypothesis = 75000
new_job_base_salary_premise = 45000
new_job_base_salary_hypothesis = 45000
commission_premise = 15
commission_hypothesis = 25

# the hypothesis talks about the salaries of the old job and the new job and the commission, all mentioned in the premise
if old_job_salary_hypothesis != old_job_salary_premise or new_job_base_salary_hypothesis != new_job_base_salary_premise:
    # check if the salaries in the hypothesis contradict the salaries reported in the premise
    label = "contradiction"
elif commission_hypothesis != commission_premise:
    # check if the commission percentage in the hypothesis contradicts the commission percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
