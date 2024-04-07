# Premise: Sid left a job paying $75,000 per year to accept a sales job paying $45,000 per year plus 15 percent commission.
# Hypothesis: Sid left a job paying $75,000 per year to accept a sales job paying $45,000 per year plus less than 55 percent commission.
# Golden Label: entailment

previous_job_premise = 75000
previous_job_hypothesis = 75000
new_job_base_salary_premise = 45000
new_job_base_salary_hypothesis = 45000
commission_premise = 15
commission_hypothesis = 55

# the hypothesis refers to the salaries and commissions mentioned in the premise
if previous_job_premise != previous_job_hypothesis or new_job_base_salary_premise != new_job_base_salary_hypothesis:
    # check if the salary values in the hypothesis contradict the premise
    label = "contradiction"
elif commission_hypothesis <= commission_premise:
    # check if the commission rate in the hypothesis contradicts the commission rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

