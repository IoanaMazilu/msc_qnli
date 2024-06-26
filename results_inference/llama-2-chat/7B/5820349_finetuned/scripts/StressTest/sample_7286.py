old_job_salary_premise = 75000
old_job_salary_hypothesis = 75000
new_job_salary_premise = 45000
new_job_salary_hypothesis = 45000
commission_premise = 15
commission_hypothesis = 55

# the hypothesis refers to the salary of the old and new job, and the commission, all mentioned in the premise
if old_job_salary_premise!= old_job_salary_hypothesis:
    # check if the salary of the old job in the hypothesis contradicts the salary of the old job reported in the premise
    label = "contradiction"
elif new_job_salary_hypothesis!= new_job_salary_premise:
    # check if the salary of the new job in the hypothesis contradicts the salary of the new job reported in the premise
    label = "contradiction"
elif commission_hypothesis!= commission_premise:
    # check if the commission in the hypothesis contradicts the commission reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
