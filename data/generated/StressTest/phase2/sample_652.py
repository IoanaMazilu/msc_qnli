# Premise: Ben left a job paying $75,000 per year to accept a sales job paying $45,000 per year plus less than 75 percent commission.
# Hypothesis: Ben left a job paying $75,000 per year to accept a sales job paying $45,000 per year plus 15 percent commission.
# Golden Label: neutral

old_job_salary = 75000
new_job_salary = 45000
new_job_commission_percentage_premise = 75
new_job_commission_percentage_hypothesis = 15

# the hypothesis refers to the salaries and commissions mentioned in the premise
if old_job_salary != new_job_salary:
    # check if the salary of the old job in the hypothesis contradicts the salary mentioned in the premise
    label = "contradiction"
elif new_job_commission_percentage_hypothesis >= new_job_commission_percentage_premise:
    # check if the commission percentage in the hypothesis contradicts the commission percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

