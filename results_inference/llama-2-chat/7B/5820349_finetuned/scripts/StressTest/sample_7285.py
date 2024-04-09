old_job_salary_premise = 75000
old_job_salary_hypothesis = 75000
new_job_salary_premise = 45000
new_job_salary_hypothesis = 45000
commission_premise = 35
commission_hypothesis = 15

# the hypothesis refers to the salary of the old and new jobs mentioned in the premise
if old_job_salary_premise!= old_job_salary_hypothesis:
    # check if the salary of the old job in the hypothesis contradicts the salary of the old job reported in the premise
    label = "contradiction"
elif new_job_salary_premise!= new_job_salary_hypothesis:
    # check if the salary of the new job in the hypothesis contradicts the salary of the new job reported in the premise
    label = "contradiction"
elif commission_premise > commission_hypothesis:
    # check if the commission percentage in the hypothesis contradicts the commission percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
