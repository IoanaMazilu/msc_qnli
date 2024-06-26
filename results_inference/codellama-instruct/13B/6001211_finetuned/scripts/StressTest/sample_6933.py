old_job_salary_premise = 75000
new_job_base_salary_premise = 45000
new_job_commission_premise = 15

old_job_salary_hypothesis = 75000
new_job_base_salary_hypothesis = 45000
new_job_commission_hypothesis = 45

# the hypothesis refers to the salaries of Jerry's old and new jobs, as well as the commission for the new job
if old_job_salary_premise!= old_job_salary_hypothesis:
    # check if the old job salary in the hypothesis contradicts the old job salary in the premise
    label = "contradiction"
elif new_job_base_salary_premise!= new_job_base_salary_hypothesis:
    # check if the new job base salary in the hypothesis contradicts the new job base salary in the premise
    label = "contradiction"
elif new_job_commission_premise > new_job_commission_hypothesis:
    # check if the new job commission in the hypothesis contradicts the new job commission in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
