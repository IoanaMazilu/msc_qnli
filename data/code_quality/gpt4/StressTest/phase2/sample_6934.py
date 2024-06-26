old_job_salary_premise = 75000
new_job_base_salary_premise = 45000
commission_percentage_premise = 45

old_job_salary_hypothesis = 75000
new_job_base_salary_hypothesis = 45000
commission_percentage_hypothesis = 15

# the hypothesis refers to the salaries and commission percentages mentioned in the premise
if old_job_salary_hypothesis != old_job_salary_premise or new_job_base_salary_hypothesis != new_job_base_salary_premise:
    # check if the salary amounts in the hypothesis contradict the salary amounts reported in the premise
    label = "contradiction"
elif commission_percentage_hypothesis >= commission_percentage_premise:
    # check if the commission percentage in the hypothesis contradicts the commission percentage estimate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
