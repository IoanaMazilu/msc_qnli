old_job_salary_premise = 75000
new_job_salary_premise = 45000
commission_premise = 0.45

old_job_salary_hypothesis = 75000
new_job_salary_hypothesis = 45000
commission_hypothesis = 0.15

# the hypothesis refers to the salaries and commission of Jerry's old and new jobs mentioned in the premise
if old_job_salary_hypothesis!= old_job_salary_premise or new_job_salary_hypothesis!= new_job_salary_premise:
    # check if the salaries in the hypothesis contradict the salaries reported in the premise
    label = "contradiction"
elif commission_hypothesis >= commission_premise:
    # check if the commission in the hypothesis contradicts the commission reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
