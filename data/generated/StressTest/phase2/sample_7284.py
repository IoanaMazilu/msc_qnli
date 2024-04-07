# Premise: John left a job paying $75,000 per year to accept a sales job paying $45,000 per year plus 15 percent commission.
# Hypothesis: John left a job paying $75,000 per year to accept a sales job paying $45,000 per year plus less than 35 percent commission.
# Golden Label: entailment

old_job_salary_premise = 75000
new_job_salary_premise = 45000
commission_premise = 15

old_job_salary_hypothesis = 75000
new_job_salary_hypothesis = 45000
commission_hypothesis = 35

# the hypothesis talks about John's old and new job salaries and commission, which are also referenced in the premise
if old_job_salary_hypothesis != old_job_salary_premise or new_job_salary_hypothesis != new_job_salary_premise:
    # check if the salaries values in the hypothesis contradict the ones in the premise
    label = "contradiction"
elif commission_hypothesis <= commission_premise:
    # check if the commission percentage in the hypothesis contradicts the commission percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

