old_job_salary_premise = 75000
old_job_salary_hypothesis = 75000
new_job_base_salary_premise = 45000
new_job_base_salary_hypothesis = 45000
new_job_commission_premise = 15
new_job_commission_hypothesis = 15

# the hypothesis refers to the salaries and commissions mentioned in the premise

if old_job_salary_hypothesis != old_job_salary_premise:
    # check if the old job salary in the hypothesis contradicts the old job salary in the premise
    label = "contradiction"
elif new_job_base_salary_hypothesis != new_job_base_salary_premise:
    # check if the new job base salary in the hypothesis contradicts the new job base salary in the premise
    label = "contradiction"
elif new_job_commission_hypothesis > new_job_commission_premise:
    # check if the new job commission in the hypothesis contradicts the new job commission in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
