old_job_salary_premise = 75000
new_job_base_salary_premise = 45000
new_job_base_salary_hypothesis = 45000

# the hypothesis talks about the base salary of John's old and new jobs, referenced also in the premise
if new_job_base_salary_hypothesis!= new_job_base_salary_premise:
    # check if the base salary of John's new job in the hypothesis contradicts the base salary of John's new job in the premise
    label = "contradiction"
else:
    # the premise gives only the base salary of John's old job
    # the base salary of John's new job is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
