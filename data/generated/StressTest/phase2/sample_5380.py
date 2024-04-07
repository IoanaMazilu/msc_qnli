# Premise: Tom left a job paying $75,000 per year to accept a sales job paying $45,000 per year plus less than 65 percent commission.
# Hypothesis: Tom left a job paying $75,000 per year to accept a sales job paying $45,000 per year plus 15 percent commission.
# Golden Label: neutral

old_job_salary = 75000
new_job_base_salary = 45000
new_job_commission_premise = 65
new_job_commission_hypothesis = 15

# The hypothesis talks about the salary and commission of Tom's old and new jobs, referenced also in the premise
if old_job_salary != 75000 or new_job_base_salary != 45000:
    # Check if the salaries mentioned in the hypothesis contradict with the premise
    label = "contradiction"
elif new_job_commission_hypothesis >= new_job_commission_premise:
    # Check if the commission percentage in the hypothesis contradicts the premise which states it is less than 65%
    label = "contradiction"
else:
    # The premise gives only an estimate for the commission percentage
    # A commission percentage less than 'new_job_commission_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

